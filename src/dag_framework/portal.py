from __future__ import annotations

from typing import Dict

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Bias Detection Portal")


evaluation_nodes: Dict[str, str] = {}
interpretation_nodes: Dict[str, str] = {}
video_models: Dict[str, str] = {}


class NodeRegistration(BaseModel):
    name: str
    description: str | None = None


class ModelRegistration(BaseModel):
    name: str
    endpoint: str


@app.post("/nodes/evaluation")
def register_evaluation(node: NodeRegistration):
    evaluation_nodes[node.name] = node.description or ""
    return {"status": "registered"}


@app.post("/nodes/interpreter")
def register_interpreter(node: NodeRegistration):
    interpretation_nodes[node.name] = node.description or ""
    return {"status": "registered"}


@app.post("/models")
def register_model(model: ModelRegistration):
    video_models[model.name] = model.endpoint
    return {"status": "registered"}
