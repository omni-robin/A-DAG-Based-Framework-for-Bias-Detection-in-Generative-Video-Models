```markdown
# DAG-Based Framework for Bias Detection in Generative Video Models

This repository contains the LaTeX source code for a research paper proposing a DAG-based framework for bias detection in generative video models.  The paper emphasizes performance evaluation across different conditions and provides a systematic, extensible, and user-driven way to ensure awareness and quantitative assessment of biases in generative AI video content.

## Overview

Generative AI models that create videos from text often reflect unintended biases in their outputs. This framework addresses this problem by providing a modular and scalable approach to evaluate and compare these biases.  The framework uses a Directed Acyclic Graph (DAG) to break down bias detection into testable components, focusing on measuring model performance across different conditions.

## Key Features

*   **DAG-Based Architecture:** Provides modularity, clarity, and a clear execution flow for bias evaluation.
*   **Semi-Automated Prompt Evolution:** Uses a language model (LLM) to generate variations of prompts for comprehensive bias testing.
*   **Multiple Video Model Support:** Enables parallel testing and comparison of API-based and local video generation models.
*   **Extensible Bias Detection Nodes:** Supports various bias categories (e.g., gender, race, age) and allows users to define custom criteria.
*   **Technical Evaluation and Scoring:** Aggregates results into a structured scoring matrix, comparing models and providing explanatory reports.
*   **Apache Airflow Implementation Example:** Provides a simplified Python code snippet demonstrating how to implement the framework using a DAG execution engine.

## Contents

*   `main.tex`:  The main LaTeX source file containing the paper's content.
*   `dag diag.png`: Image showing a DAG diagram for bias evaluation.
*   `seqex.png`: Image showing the sequence of steps in the bias detection pipeline.

## Dependencies

To compile the LaTeX document, you will need the following:

*   A LaTeX distribution (e.g., TeX Live, MiKTeX).
*   The following LaTeX packages:
    *   `inputenc`
    *   `graphicx`
    *   `authblk`
    *   `listings`
    *   `minted`
    *   `caption`
    *   `hyperref`

## Compilation

To compile the `main.tex` file into a PDF, use the following command:

```bash
pdflatex main.tex
bibtex main  # Only needed if you switch to BibTeX
pdflatex main.tex
pdflatex main.tex
```

**Note:**  The `pdflatex` command (or equivalent for your LaTeX distribution) may need to be run multiple times to resolve all references and citations correctly.  The `bibtex` command is only needed if you change the reference style to use BibTeX instead of the included `thebibliography` environment.

## References

The references are explicitly included within the `thebibliography` environment in the `main.tex` file.  To add or modify references, edit this section directly.  (See the LaTeX source for details.)

## Example Scoring Matrix

```
| Bias Category             | Model A | Model B | Model C |
| ------------------------- | ------- | ------- | ------- |
| Gender Representation (score/10) | 3.5     | 7.5     | 9.0     |
| Racial Diversity (score/10)    | 4.0     | 5.5     | 8.0     |
| Age Diversity (score/10)       | 2.0     | 5.0     | 6.5     |
```

Higher scores indicate more balanced representation.

## License

This project is licensed under the [Insert License Here] - see the `LICENSE` file for details (if you have one).

## Contributing

Contributions are welcome! Please submit a pull request with your changes.

## Authors

*   Robin Nilsson
*   Valerie Veatch

## Contact

[Your Email Address]
```
