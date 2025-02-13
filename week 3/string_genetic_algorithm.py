import random
import string

# Parameters
TARGET_STRING = "HELLO_WORLD"
POPULATION_SIZE = 100
MUTATION_RATE = 0.01
GENERATIONS = 1000

# Generate a random string of fixed length
def generate_random_string(length):
    return ''.join(random.choice(string.ascii_uppercase + "_") for _ in range(length))

# Calculate fitness (number of matching characters)
def calculate_fitness(individual):
    return sum(1 for a, b in zip(individual, TARGET_STRING) if a == b)

# Select parents using tournament selection
def select_parent(population):
    tournament_size = 5
    tournament = random.sample(population, tournament_size)
    return max(tournament, key=lambda x: x[1])

# Perform crossover (single-point crossover)
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(TARGET_STRING) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Perform mutation
def mutate(individual):
    individual = list(individual)
    for i in range(len(individual)):
        if random.random() < MUTATION_RATE:
            individual[i] = random.choice(string.ascii_uppercase + "_")
    return ''.join(individual)

# Main Genetic Algorithm
def genetic_algorithm():
    # Step 1: Initialisation
    population = [(generate_random_string(len(TARGET_STRING)), 0) for _ in range(POPULATION_SIZE)]
    
    for generation in range(GENERATIONS):
        # Step 2: Fitness Assignment
        population = [(individual, calculate_fitness(individual)) for individual, _ in population]
        
        # Step 3: Selection
        parents = [select_parent(population) for _ in range(POPULATION_SIZE)]
        
        # Step 4: Crossover
        offspring = []
        for i in range(0, POPULATION_SIZE, 2):
            parent1, parent2 = parents[i], parents[i + 1]
            child1, child2 = crossover(parent1[0], parent2[0])
            offspring.append((child1, 0))
            offspring.append((child2, 0))
        
        # Step 5: Mutation
        offspring = [(mutate(individual), 0) for individual, _ in offspring]
        
        # Step 6: Replacement
        population = offspring
        
        # Step 7: Termination Condition
        best_individual = max(population, key=lambda x: x[1])
        print(f"Generation {generation}: Best Individual = {best_individual[0]}, Fitness = {best_individual[1]}")
        
        if best_individual[0] == TARGET_STRING:
            print("Target string found!")
            break

# Run the genetic algorithm
if __name__ == "__main__":
    genetic_algorithm()