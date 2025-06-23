from dag_framework import GenderBiasNode, Frame
from PIL import Image

def generate_synthetic_faces(male, female):
    frames = []
    for _ in range(male):
        frames.append(Frame(Image.new("RGB", (10, 10), color=(255, 0, 0)), None))
    for _ in range(female):
        frames.append(Frame(Image.new("RGB", (10, 10), color=(0, 0, 255)), None))
    return frames


def dummy_detector(image):
    w, h = image.size
    return [(0, 0, w, h)]


def dummy_classifier(image):
    pixel = image.getpixel((0, 0))
    if pixel == (255, 0, 0):
        return "male", 1.0
    else:
        return "female", 1.0


def test_gender_node_balanced():
    frames = generate_synthetic_faces(5, 5)
    node = GenderBiasNode(detector=dummy_detector, classifier=dummy_classifier)
    result = node.run(frames)
    assert result["metrics"]["parity_score"] == 1.0
    assert result["passed"] is True

