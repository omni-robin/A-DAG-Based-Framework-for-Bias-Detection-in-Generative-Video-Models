class Node:
    """Base class for DAG nodes."""

    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def run(self, data):
        """Execute this node's logic.

        Subclasses should override this method.
        """
        raise NotImplementedError()


class BiasDefinitionNode(Node):
    """Node that defines the bias to detect."""

    def __init__(self, name, description):
        super().__init__(name)
        self.description = description

    def run(self, data=None):
        return {"bias": self.description}


class AnalyticsNode(Node):
    """Node that analyzes data for bias."""

    def __init__(self, name, analyzer_fn):
        super().__init__(name)
        self.analyzer_fn = analyzer_fn

    def run(self, data):
        return self.analyzer_fn(data)
