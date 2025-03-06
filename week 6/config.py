class Config:
    """Class representing configuration parameters for the ocean simulation."""

    # Simulation Settings
    SIM_NAME = "Ocean Simulation"
    OCEAN_SIZE = 20  # Grid size (N x N)

    # Colours for Agents
    SHARK_COLOR = "red"
    SARDINE_COLOR = "blue"
    PLANKTON_COLOR = "green"

    # Breeding Probabilities
    SHARK_BREED_PROB = 0.1  # Probability of a shark reproducing
    SARDINE_BREED_PROB = 0.2  # Probability of a sardine reproducing

    # Energy Levels (Optional, useful for aging & survival)
    SHARK_ENERGY_GAIN = 5  # Energy gained when eating a sardine
    SARDINE_ENERGY_GAIN = 3  # Energy gained when eating plankton
    SHARK_LIFESPAN = 50  # Maximum lifespan for sharks
    SARDINE_LIFESPAN = 30  # Maximum lifespan for sardines
