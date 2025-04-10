import networkx as nx
import matplotlib.pyplot as plt

class SocialNetwork:
    def __init__(self):
        """Initialize the social network graph"""
        self.graph = nx.DiGraph()
        self.node_positions = None

    def add_users(self, users):
        """Add multiple users to the network"""
        self.graph.add_nodes_from(users)

    def add_followings(self, follow_relations):
        """Add directed edges representing follow relationships"""
        self.graph.add_edges_from(follow_relations)

    def visualize_network(self):
        """Visualize the social network with matplotlib"""
        # Calculate node positions using spring layout
        self.node_positions = nx.spring_layout(self.graph, seed=42, k=0.9)
        
        # Create figure
        plt.figure(figsize=(10, 8))
        
        # Draw nodes and edges
        nx.draw_networkx_nodes(
            self.graph, 
            self.node_positions,
            node_size=2000,
            node_color='lightblue',
            alpha=0.9
        )
        
        nx.draw_networkx_edges(
            self.graph,
            self.node_positions,
            edge_color='gray',
            arrows=True,
            arrowstyle='->',
            arrowsize=20,
            width=1.5
        )
        
        # Draw labels
        nx.draw_networkx_labels(
            self.graph,
            self.node_positions,
            font_size=12,
            font_weight='bold'
        )
        
        # Add title and display
        plt.title("Social Network Analysis: Follow Relationships", fontsize=14)
        plt.axis('off')
        plt.tight_layout()
        plt.show()

    def analyze_network(self):
        """Perform basic network analysis"""
        print("\nNetwork Analysis:")
        print(f"Number of users: {self.graph.number_of_nodes()}")
        print(f"Number of follow relationships: {self.graph.number_of_edges()}")
        
        # Calculate in-degree (number of followers)
        in_degrees = dict(self.graph.in_degree())
        top_influencers = sorted(in_degrees.items(), key=lambda x: x[1], reverse=True)[:3]
        
        print("\nTop Influencers (most followers):")
        for user, count in top_influencers:
            print(f"{user}: {count} followers")

def main():
    """Main function to create and analyze the social network"""
    # Create social network
    network = SocialNetwork()
    
    # Define users
    users = ["Ananya", "Raj", "Yuki", "Kai", "Aisha", "Luca"]
    
    # Define follow relationships
    follow_relations = [
        ("Ananya", "Raj"),
        ("Ananya", "Yuki"),
        ("Raj", "Yuki"),
        ("Yuki", "Ananya"),
        ("Yuki", "Kai"),
        ("Kai", "Aisha"),
        ("Aisha", "Luca"),
        ("Luca", "Raj"),
        ("Luca", "Ananya")
    ]
    
    # Build the network
    network.add_users(users)
    network.add_followings(follow_relations)
    
    # Visualize and analyze
    network.visualize_network()
    network.analyze_network()

if __name__ == "__main__":
    main()