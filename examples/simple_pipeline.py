from dag_framework.node import BiasDefinitionNode, AnalyticsNode


def count_female_terms(text):
    female_terms = ["she", "her", "woman"]
    return {"female_term_count": sum(text.lower().count(t) for t in female_terms)}


def main():
    bias_node = BiasDefinitionNode("gender_bias", "Counts female-gendered terms")

    analytics_node = AnalyticsNode("count_female_terms", count_female_terms)

    # Example data
    sample_text = "She is a woman. Her actions are great."

    print(bias_node.run())
    print(analytics_node.run(sample_text))


if __name__ == "__main__":
    main()
