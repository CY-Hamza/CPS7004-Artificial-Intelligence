from bayesian_network import BayesianNetwork
from node import Node

def main():
    # Create a Bayesian Network
    network = BayesianNetwork()

    # Add nodes
    cold_weather = network.add_node("Cold Weather")
    lack_of_sleep = network.add_node("Lack of Sleep")
    getting_sick = network.add_node("Getting Sick")

    # Add edges
    network.add_edge("Cold Weather", "Getting Sick")
    network.add_edge("Lack of Sleep", "Getting Sick")

    # Define CPTs
    # Cold Weather: P(Cold Weather = Yes) = 0.3, P(Cold Weather = No) = 0.7
    cold_weather.set_cpt({
        (): 0.3  # No parents, so the key is an empty tuple
    })

    # Lack of Sleep: P(Lack of Sleep = Yes) = 0.4, P(Lack of Sleep = No) = 0.6
    lack_of_sleep.set_cpt({
        (): 0.4  # No parents, so the key is an empty tuple
    })

    # Getting Sick: P(Getting Sick = Yes | Cold Weather, Lack of Sleep)
    getting_sick.set_cpt({
        (True, True): 0.6,  # Cold Weather = Yes, Lack of Sleep = Yes
        (True, False): 0.4,  # Cold Weather = Yes, Lack of Sleep = No
        (False, True): 0.3,  # Cold Weather = No, Lack of Sleep = Yes
        (False, False): 0.1,  # Cold Weather = No, Lack of Sleep = No
    })

    # Print network details
    print("Bayesian Network Setup:")
    for name, node in network.get_nodes().items():
        print(f"Node: {name}")
        print(f"  Parents: {[parent.get_name() for parent in node.get_parents()]}")
        print(f"  CPT: {node.get_cpt()}")

if __name__ == "__main__":
    main()