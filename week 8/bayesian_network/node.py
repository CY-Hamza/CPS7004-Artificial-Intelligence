from typing import List, Dict, Tuple, Optional

class Node:
    def __init__(self, name: str):
        """
        Initialize a Node.

        Args:
            name (str): The name of the node.
        """
        self.name = name  # Name of the node
        self.parents: List['Node'] = []  # List of parent nodes
        self.cpt: Dict[Tuple[bool, ...], float] = {}  # Conditional Probability Table (CPT)

    def add_parent(self, parent: 'Node') -> None:
        """
        Add a parent node to the current node.

        Args:
            parent (Node): The parent node to add.
        """
        if parent not in self.parents:
            self.parents.append(parent)

    def remove_parent(self, parent: 'Node') -> None:
        """
        Remove a parent node from the current node.

        Args:
            parent (Node): The parent node to remove.
        """
        if parent in self.parents:
            self.parents.remove(parent)

    def set_cpt(self, cpt: Dict[Tuple[bool, ...], float]) -> None:
        """
        Set the Conditional Probability Table (CPT) for the node.

        Args:
            cpt (Dict[Tuple[bool, ...], float]): The CPT to set.
        """
        self.cpt = cpt

    def get_name(self) -> str:
        """
        Get the name of the node.

        Returns:
            str: The name of the node.
        """
        return self.name

    def get_parents(self) -> List['Node']:
        """
        Get the list of parent nodes.

        Returns:
            List[Node]: The list of parent nodes.
        """
        return self.parents

    def get_cpt(self) -> Dict[Tuple[bool, ...], float]:
        """
        Get the Conditional Probability Table (CPT).

        Returns:
            Dict[Tuple[bool, ...], float]: The CPT.
        """
        return self.cpt