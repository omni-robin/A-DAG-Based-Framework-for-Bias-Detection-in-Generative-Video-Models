from dag_framework.node import BiasDefinitionNode, AnalyticsNode
from dag_framework.gender_bias import GenderBiasNode, Frame
from PIL import Image


def count_female_terms(text):
    female_terms = ["she", "her", "woman"]
    return {"female_term_count": sum(text.lower().count(t) for t in female_terms)}


def main():
    bias_node = BiasDefinitionNode("gender_bias", "Counts female-gendered terms")

    analytics_node = AnalyticsNode("count_female_terms", count_female_terms)

    # Demonstrate GenderBiasNode on two simple frames
    frames = [
        Frame(Image.new("RGB", (10, 10), color=(255, 0, 0))),
        Frame(Image.new("RGB", (10, 10), color=(0, 0, 255))),
    ]
    gb_node = GenderBiasNode(detector=lambda img: [(0, 0, img.size[0], img.size[1])],
                              classifier=lambda img: ("male" if img.getpixel((0, 0))[0] > 0 else "female", 1.0))

    # Example data
    sample_text = "She is a woman. Her actions are great."

    print(bias_node.run())
    print(analytics_node.run(sample_text))
    print(gb_node.run(frames))


if __name__ == "__main__":
    main()

