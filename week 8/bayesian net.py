# Create a Bayesian Network
network = BayesianNetwork()

# Add nodes
cold_weather = network.add_node("Cold Weather")
lack_of_sleep = network.add_node("Lack of Sleep")
getting_sick = network.add_node("Getting Sick")

# Add edges
network.add_edge("Cold Weather", "Getting Sick")
network.add_edge("Lack of Sleep", "Getting Sick")

# Print network details
print("Nodes in the network:")
for name, node in network.get_nodes().items():
    print(f"Node: {name}, Parents: {[parent.get_name() for parent in node.get_parents()]}")