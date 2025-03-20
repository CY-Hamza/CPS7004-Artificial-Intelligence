import networkx as nx
import matplotlib.pyplot as plt

class Visualiser:
    def __init__(self, bayesian_network):
        """
        Initialize the Visualiser with a Bayesian Network.

        Args:
            bayesian_network: The Bayesian Network to visualize.
        """
        self.bayesian_network = bayesian_network

    def visualise(self, cpts=None):
        """
        Visualize the Bayesian Network using NetworkX and Matplotlib.

        Args:
            cpts (dict, optional): A dictionary of CPTs for each node. Defaults to None.
        """
        # Create a directed graph
        graph = nx.DiGraph()

        # Add nodes and edges to the graph
        for node_name, node in self.bayesian_network.get_nodes().items():
            graph.add_node(node_name)
            for parent in node.get_parents():
                graph.add_edge(parent.get_name(), node_name)

        # Draw the graph
        pos = nx.spring_layout(graph)  # Layout for positioning nodes
        nx.draw(graph, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=10, font_weight="bold", arrows=True)

        # Add CPTs as text below each node
        if cpts:
            for node_name, cpt in cpts.items():
                x, y = pos[node_name]
                plt.text(x, y - 0.15, f"CPT: {cpt}", fontsize=8, ha="center")

        # Display the graph
        plt.show()