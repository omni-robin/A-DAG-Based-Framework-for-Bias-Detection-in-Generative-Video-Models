
# DAG-Based Framework for Bias Detection in Generative Video Models

This repository contains a Directed Acyclic Graph (DAG)-based framework designed to detect and mitigate biases in generative video models. Our work addresses the growing concern that AI-generated videos can perpetuate and amplify societal biases, particularly regarding gender, race, age, and other sensitive attributes.

## Introduction

Generative AI video models, while powerful, are trained on vast datasets that often reflect existing societal inequalities.  This can lead to models producing outputs that reinforce stereotypes and underrepresent certain groups. Our framework offers a systematic way to:

*   **Evaluate** the extent of bias in different video generation models.
*   **Compare** the performance of various models in generating diverse and representative content.
*   **Provide insights** that can guide model developers in mitigating biases and improving fairness.

## Core Components

Our framework leverages a modular DAG architecture, where each node performs a specific task in the bias detection pipeline. Key components include:

*   **Prompt Generation:** A semi-automated process that uses Language Models (LLMs) to generate diverse prompts to probe for biases.  Starting from a base prompt, the system creates variations that emphasize different attributes like gender, ethnicity, and age.
*   **Video Generation:** Executes the generated prompts on various generative video models (both local and API-based) to produce video outputs.
*   **Content Extraction:** Analyzes the generated videos to extract relevant information, such as key frames and textual descriptions generated using vision-language models.
*   **Bias Analysis:** Employs dedicated modules to analyze the extracted content for different types of biases, including gender stereotypes, racial representation imbalances, and age representation disparities.  These modules produce quantitative indicators of bias.
*   **Aggregation & Reporting:**  Aggregates the results from all analysis modules into a structured scoring matrix, comparing model performance and providing explanatory reports detailing the detected biases.

## Key Benefits

*   **Modularity and Extensibility:** The DAG structure allows for easy addition or modification of bias detection modules. New bias categories can be integrated without overhauling the entire system.
*   **Comprehensive Evaluation:** The framework ensures that models are evaluated under a wide range of conditions using diverse prompts.
*   **Quantitative and Explainable Results:** The framework provides quantitative scores and explanatory reports that allow for a deeper understanding of the types of biases present in different models.
*   **Fair Comparison:** The framework ensures that all models are evaluated under identical conditions, allowing for a fair comparison of their performance.

## Getting Started

This repository primarily houses the theoretical framework and a high-level implementation example. The detailed implementation is complex and distributed across different systems. This repository is intended to demonstrate our work.

## Future Work

We are currently exploring integrating this framework with decentralized and privacy-preserving platforms. Specifically, we are investigating the possibility of deploying this bias detection pipeline within:

*   **Torus Network:** Torus is envisioned as a Layer1 self-assembling and self-optimizing autonomous super-swarm. Integrating our framework within Torus could allow the bias detection pipeline to become a self-organizing component within a larger, dynamically evolving ecosystem. This means the bias detection process itself could be optimized and adapted based on the incentives and permissions managed by the Torus swarm, leading to a more resilient and adaptive bias mitigation strategy.
*   **JAM (JOIN-ACCUMULATE MACHINE):** JAM, as a formal system focused on set operations, dictionaries, and tuples, provides a foundation for reasoning about and implementing our bias detection pipeline. We envision encoding the data structures and algorithms used in our framework within JAM to rigorously define and verify its behavior. For example, the aggregation of bias scores could be formally specified as a JOIN-ACCUMULATE operation. This could enable us to prove properties about the correctness and fairness of the bias detection process, and to optimize the framework for efficient execution. Furthermore, the permissions and incentivized participation in the Torus architecture can use JAM to more formally verify the agents actions and access.
*   **Bittensor:** A decentralized, blockchain-based machine learning network. Deploying bias detection on Bittensor could leverage the network's distributed compute resources for large-scale bias analysis, allowing for cost-effective and scalable bias evaluation and fostering a more equitable AI ecosystem.

These integrations aim to enhance the transparency, accountability, and fairness of generative video models by leveraging blockchain technology and decentralized computation. Further research will focus on adapting the framework for these environments, addressing challenges related to data privacy, computational cost, and decentralized governance.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Authors

*   Robin Nilsson
*   Valerie Veatch

## Contact

rnilsson@oplyt.com
