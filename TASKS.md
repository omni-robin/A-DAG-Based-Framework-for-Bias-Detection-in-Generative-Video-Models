# Development Tasks

This document lists initial tasks to build the DAG-based bias detection framework.

## 1. Implement Core DAG Structure
- Create a `Node` base class supporting child nodes and a `run` method.
- Provide subclasses like `BiasDefinitionNode` and `AnalyticsNode`.

## 2. Build Sample Analytics
- Implement simple analytics functions (e.g., word counts) demonstrating how to detect bias.
- Provide an example pipeline in `examples/` that composes nodes and runs analytics on sample data.

These tasks will form the foundation for more advanced bias detection modules.
