from pathlib import Path
from dag_framework import GenderBiasNode, run_video_analytics
from PIL import Image


def dummy_detector(image):
    w, h = image.size
    return [(0, 0, w, h)]


def dummy_classifier(image):
    pixel = image.getpixel((0, 0))
    return ("male", 1.0) if pixel == (255, 0, 0) else ("female", 1.0)


def create_sample_gif(path: Path):
    frame1 = Image.new("RGB", (10, 10), color=(255, 0, 0))
    frame2 = Image.new("RGB", (10, 10), color=(0, 0, 255))
    frame1.save(path, save_all=True, append_images=[frame2], loop=0, duration=100)


def test_run_video_analytics(tmp_path: Path):
    video_path = tmp_path / "sample.gif"
    create_sample_gif(video_path)

    node = GenderBiasNode(detector=dummy_detector, classifier=dummy_classifier)
    results = run_video_analytics(str(video_path), [node], tmp_path)

    assert results[node.name]["metrics"]["male_count"] == 1
    assert results[node.name]["metrics"]["female_count"] == 1
    assert (tmp_path / "report.json").exists()
