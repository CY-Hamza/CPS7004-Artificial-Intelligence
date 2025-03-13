import unittest
from particle import Particle

class TestParticle(unittest.TestCase):
    def test_initialization(self):
        # Define bounds and a simple objective function
        bounds = [(-5.0, 5.0), (-5.0, 5.0)]
        objective_function = lambda x: sum(xi**2 for xi in x)

        # Create a particle
        particle = Particle(bounds, objective_function)

        # Check if position is within bounds
        for i, pos in enumerate(particle.get_position()):
            self.assertTrue(bounds[i][0] <= pos <= bounds[i][1])

        # Check if velocity is initialized to zero
        self.assertEqual(particle.get_velocity(), [0.0, 0.0])

        # Check if personal best is initialized correctly
        p_best_position, p_best_value = particle.get_personal_best()
        self.assertEqual(p_best_position, particle.get_position())
        self.assertEqual(p_best_value, objective_function(particle.get_position()))

    def test_update_personal_best(self):
        # Define bounds and a simple objective function
        bounds = [(-5.0, 5.0), (-5.0, 5.0)]
        objective_function = lambda x: sum(xi**2 for xi in x)

        # Create a particle with a specific initial position
        initial_position = [1.0, 2.0]
        particle = Particle(bounds, objective_function, initial_position)

        # Update position to a better value
        particle.position = [0.5, 1.0]
        particle.update_personal_best()

        # Check if personal best is updated
        p_best_position, p_best_value = particle.get_personal_best()
        self.assertEqual(p_best_position, [0.5, 1.0])
        self.assertEqual(p_best_value, objective_function([0.5, 1.0]))

if __name__ == "__main__":
    unittest.main()