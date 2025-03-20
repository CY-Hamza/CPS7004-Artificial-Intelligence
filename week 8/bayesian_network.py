from typing import Dict
from node import Node

class BayesianNetwork:
    def __init__(self):
        """
        Initialize a Bayesian Network.
        """
        self.nodes: Dict[str, Node] = {}  # Dictionary to store nodes by name

    def add_node(self, name: str) -> Node:
        """
        Add a node to the Bayesian Network.

        Args:
            name (str): The name of the node.

        Returns:
            Node: The newly created node.
        """
        if name in self.nodes:
            raise ValueError(f"Node with name '{name}' already exists.")
        node = Node(name)
        self.nodes[name] = node
        return node

    def add_edge(self, parent_name: str, child_name: str) -> None:
        """
        Add a directed edge from a parent node to a child node.

        Args:
            parent_name (str): The name of the parent node.
            child_name (str): The name of the child node.
        """
        if parent_name not in self.nodes:
            raise ValueError(f"Parent node '{parent_name}' does not exist.")
        if child_name not in self.nodes:
            raise ValueError(f"Child node '{child_name}' does not exist.")
        
        parent_node = self.nodes[parent_name]
        child_node = self.nodes[child_name]
        child_node.add_parent(parent_node)

    def get_node(self, name: str) -> Node:
        """
        Get a node by its name.

        Args:
            name (str): The name of the node.

        Returns:
            Node: The node with the specified name.
        """
        if name not in self.nodes:
            raise ValueError(f"Node with name '{name}' does not exist.")
        return self.nodes[name]

    def get_nodes(self) -> Dict[str, Node]:
        """
        Get all nodes in the Bayesian Network.

        Returns:
            Dict[str, Node]: A dictionary of all nodes, keyed by name.
        """
        return self.nodes