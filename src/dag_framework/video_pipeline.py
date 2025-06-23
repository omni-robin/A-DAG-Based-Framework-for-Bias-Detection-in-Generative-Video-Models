import os
import json
from typing import Iterable, List

import imageio.v2 as imageio
from PIL import Image

from .gender_bias import Frame
from .node import Node, AnalyticsNode


def read_video_frames(video_path: str) -> List[Frame]:
    """Load video frames from ``video_path`` as ``Frame`` objects."""
    reader = imageio.get_reader(video_path)
    frames = [Frame(Image.fromarray(frame)) for frame in reader]
    reader.close()
    return frames


def run_video_analytics(
    video_path: str,
    analytics_nodes: Iterable[AnalyticsNode],
    bucket_dir: str | None = None,
) -> dict[str, dict]:
    """Run analytics nodes on the video and optionally store results.

    Parameters
    ----------
    video_path:
        Path to the video file to analyze.
    analytics_nodes:
        Iterable of ``AnalyticsNode`` instances.
    bucket_dir:
        Optional directory representing a storage bucket where results
        will be written as ``report.json``.
    """
    frames = read_video_frames(video_path)
    results: dict[str, dict] = {}
    for node in analytics_nodes:
        results[node.name] = node.run(frames)

    if bucket_dir is not None:
        os.makedirs(bucket_dir, exist_ok=True)
        report_path = os.path.join(bucket_dir, "report.json")
        with open(report_path, "w", encoding="utf-8") as fh:
            json.dump(results, fh, indent=2)

    return results
