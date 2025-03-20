import unittest
from node import Node

class TestNode(unittest.TestCase):
    def test_initialization(self):
        # Create a node
        node = Node("Cold Weather")

        # Check if attributes are initialized correctly
        self.assertEqual(node.get_name(), "Cold Weather")
        self.assertEqual(node.get_parents(), [])
        self.assertEqual(node.get_cpt(), {})

    def test_add_parent(self):
        # Create nodes
        parent_node = Node("Lack of Sleep")
        child_node = Node("Getting Sick")

        # Add parent
        child_node.add_parent(parent_node)

        # Check if parent is added
        self.assertEqual(child_node.get_parents(), [parent_node])

    def test_remove_parent(self):
        # Create nodes
        parent_node = Node("Lack of Sleep")
        child_node = Node("Getting Sick")

        # Add and then remove parent
        child_node.add_parent(parent_node)
        child_node.remove_parent(parent_node)

        # Check if parent is removed
        self.assertEqual(child_node.get_parents(), [])

    def test_set_cpt(self):
        # Create a node
        node = Node("Getting Sick")

        # Define a CPT
        cpt = {
            (True, True): 0.6,  # Cold Weather = True, Lack of Sleep = True
            (True, False): 0.4,  # Cold Weather = True, Lack of Sleep = False
            (False, True): 0.3,  # Cold Weather = False, Lack of Sleep = True
            (False, False): 0.1,  # Cold Weather = False, Lack of Sleep = False
        }

        # Set CPT
        node.set_cpt(cpt)

        # Check if CPT is set correctly
        self.assertEqual(node.get_cpt(), cpt)

if __name__ == "__main__":
    unittest.main()