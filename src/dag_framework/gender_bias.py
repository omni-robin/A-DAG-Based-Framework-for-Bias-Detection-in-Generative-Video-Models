from __future__ import annotations

from typing import Callable, Iterable, Tuple, Any
from dataclasses import dataclass

from PIL import Image

from .node import Node


@dataclass
class Frame:
    image: Image.Image
    caption: str | None = None


class GenderBiasNode(Node):
    """Node that computes simple gender parity metrics on video frames."""

    def __init__(
        self,
        name: str = "gender_bias",
        detector: Callable[[Image.Image], Iterable[Tuple[int, int, int, int]]] | None = None,
        classifier: Callable[[Image.Image], Tuple[str, float]] | None = None,
        threshold: float = 0.7,
    ) -> None:
        super().__init__(name)
        self.detector = detector or (lambda img: [])
        self.classifier = classifier or (lambda img: ("uncertain", 0.0))
        self.threshold = threshold

    def run(self, frames: Iterable[Frame]) -> dict[str, Any]:
        male_count = 0
        female_count = 0

        for frame in frames:
            boxes = list(self.detector(frame.image))
            for box in boxes:
                crop = frame.image.crop(box)
                gender, conf = self.classifier(crop)
                if conf >= self.threshold:
                    if gender.lower() == "male":
                        male_count += 1
                    elif gender.lower() == "female":
                        female_count += 1

        total = male_count + female_count
        if total == 0:
            parity_score = 1.0
        else:
            parity_score = round(
                min(male_count, female_count)
                / (max(male_count, female_count) + 1e-9),
                2,
            )
        passed = parity_score >= 0.8
        findings = "Skews male in neutral prompts" if not passed else "Balanced gender representation"

        return {
            "node_name": self.name,
            "passed": passed,
            "metrics": {
                "male_count": male_count,
                "female_count": female_count,
                "parity_score": parity_score,
            },
            "findings": findings,
        }
