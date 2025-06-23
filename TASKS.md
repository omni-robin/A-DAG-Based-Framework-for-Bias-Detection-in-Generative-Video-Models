# Development Tasks

This document tracks the major tasks for the project and their status.

## Completed

* Implement the core DAG structure with `Node`, `BiasDefinitionNode`, and `AnalyticsNode` classes.
* Create sample analytics functions and an example pipeline under `examples/`.
* Add a `GenderBiasNode` with unit tests.
* Provide a video analytics helper for running nodes on video files.
* Implement a simple prompt evolution module.
* Add a minimal FastAPI portal for registering nodes and models.

## Next Steps

* Expand analytics nodes (e.g., racial and age bias detectors).
* Aggregate results from multiple nodes into a scoring matrix.
* Increase test coverage for the portal and prompt evolution functions.
* Document a full evaluation workflow using the portal and analytics nodes.
* Investigate integration with decentralized platforms such as Torus, JAM and Bittensor.
