import random
from typing import List, Tuple, Callable

class Particle:
    def __init__(
        self,
        bounds: List[Tuple[float, float]],
        objective_function: Callable[[List[float]], float],
        initial_position: List[float] = None,
    ):
        """
        Initialize a Particle.

        Args:
            bounds (List[Tuple[float, float]]): Bounds for each dimension as a list of tuples (min, max).
            objective_function (Callable[[List[float]], float]): Objective function to minimize.
            initial_position (List[float], optional): Initial position of the particle. Defaults to random.
        """
        # Store the bounds and determine the number of dimensions
        self.bounds = bounds
        self.dimensions = len(bounds)

        # Initialize position
        if initial_position is not None:
            self.position = initial_position
        else:
            self.position = [random.uniform(b[0], b[1]) for b in bounds]

        # Initialize velocity to zero
        self.velocity = [0.0 for _ in range(self.dimensions)]

        # Initialize personal best position and value
        self.p_best_position = self.position.copy()
        self.p_best_value = objective_function(self.position)

        # Store the objective function
        self.objective_function = objective_function

    def update_personal_best(self) -> None:
        """
        Update the particle's personal best position and value based on the current position.
        """
        current_value = self.objective_function(self.position)
        if current_value < self.p_best_value:
            self.p_best_position = self.position.copy()
            self.p_best_value = current_value

    def update_position(self) -> None:
        """
        Update the particle's position based on its current velocity.
        Ensure the new position remains within the specified bounds.
        """
        for i in range(self.dimensions):
            # Update position
            self.position[i] += self.velocity[i]

            # Clamp position to bounds
            self.position[i] = max(self.bounds[i][0], min(self.bounds[i][1], self.position[i]))

    def get_position(self) -> List[float]:
        """
        Get the particle's current position.

        Returns:
            List[float]: The particle's current position.
        """
        return self.position

    def get_velocity(self) -> List[float]:
        """
        Get the particle's current velocity.

        Returns:
            List[float]: The particle's current velocity.
        """
        return self.velocity

    def get_personal_best(self) -> Tuple[List[float], float]:
        """
        Get the particle's personal best position and value.

        Returns:
            Tuple[List[float], float]: Personal best position and value.
        """
        return self.p_best_position, self.p_best_value