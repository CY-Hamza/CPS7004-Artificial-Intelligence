import time
from typing import Dict, Type

from view.gui import Gui
from model.ocean import Ocean
from model.agents import Shark, Sardine, Plankton


class Simulator:
    """Class representing a simulator."""

    def __init__(self) -> None:
        """
        Initialise the Simulator object.

        Initialises the environment, and generates the initial population of agents.
        """
        self.__ocean = Ocean()
        self.__agents = []
        self.__generate_initial_population()
        self.__is_running = False

        # Define a dictionary mapping agent classes to their respective colours
        self.__agent_colours: Dict[Type, str] = {
            Shark: "gray",
            Sardine: "blue",
            Plankton: "green"
        }

        # Initialise a new Gui object
        self.__gui = Gui(self.__ocean, self.__agent_colours)

        # Render the GUI
        self.__render()

    def __generate_initial_population(self) -> None:
        """
        Generate the initial population of agents in the ocean.
        """
        # TODO: Implement agent placement logic
        pass

    def run(self) -> None:
        """Run the simulation loop."""
        self.__is_running = True

        while self.__is_running:
            self.__update()
            self.__render()
            time.sleep(1)

            if self.__gui.is_closed():
                self.__is_running = False

    def __render(self) -> None:
        """Render the current state of the simulation in the GUI."""
        self.__gui.render()

    def __update(self) -> None:
        """Update the simulation state by making each agent act."""
        for agent in self.__agents:
            agent.act()


if __name__ == "__main__":
    """
    Entry point for running the simulation.
    """
    simulation = Simulator()
    simulation.run()
