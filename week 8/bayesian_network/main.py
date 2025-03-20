from bayesian_network import BayesianNetwork
from node import Node
from visualiser import Visualiser

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
    cold_weather.set_cpt({
        (): 0.3  # No parents, so the key is an empty tuple
    })
    lack_of_sleep.set_cpt({
        (): 0.4  # No parents, so the key is an empty tuple
    })
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

    # Visualize the Bayesian Network
    cpts = {
        "Cold Weather": {(): 0.3},
        "Lack of Sleep": {(): 0.4},
        "Getting Sick": {
            (True, True): 0.6,
            (True, False): 0.4,
            (False, True): 0.3,
            (False, False): 0.1,
        },
    }
    visualiser = Visualiser(network)
    visualiser.visualise(cpts=cpts)

if __name__ == "__main__":
    main()
    