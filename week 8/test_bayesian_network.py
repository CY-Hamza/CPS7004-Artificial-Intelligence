import unittest
from bayesian_network import BayesianNetwork
from node import Node

class TestBayesianNetwork(unittest.TestCase):
    def test_initialization(self):
        # Create a Bayesian Network
        network = BayesianNetwork()

        # Check if nodes dictionary is empty
        self.assertEqual(network.get_nodes(), {})

    def test_add_node(self):
        # Create a Bayesian Network
        network = BayesianNetwork()

        # Add a node
        node = network.add_node("Cold Weather")

        # Check if node is added
        self.assertEqual(network.get_nodes(), {"Cold Weather": node})

    def test_add_edge(self):
        # Create a Bayesian Network
        network = BayesianNetwork()

        # Add nodes
        parent_node = network.add_node("Cold Weather")
        child_node = network.add_node("Getting Sick")

        # Add an edge
        network.add_edge("Cold Weather", "Getting Sick")

        # Check if edge is added
        self.assertEqual(child_node.get_parents(), [parent_node])

    def test_get_node(self):
        # Create a Bayesian Network
        network = BayesianNetwork()

        # Add a node
        node = network.add_node("Cold Weather")

        # Retrieve the node
        retrieved_node = network.get_node("Cold Weather")

        # Check if the correct node is retrieved
        self.assertEqual(retrieved_node, node)

    def test_add_existing_node(self):
        # Create a Bayesian Network
        network = BayesianNetwork()

        # Add a node
        network.add_node("Cold Weather")

        # Try to add the same node again
        with self.assertRaises(ValueError):
            network.add_node("Cold Weather")

    def test_add_edge_with_nonexistent_node(self):
        # Create a Bayesian Network
        network = BayesianNetwork()

        # Add a node
        network.add_node("Cold Weather")

        # Try to add an edge with a nonexistent child node
        with self.assertRaises(ValueError):
            network.add_edge("Cold Weather", "Getting Sick")

if __name__ == "__main__":
    unittest.main()