# 1. Implement Genetic algorithm for the Maxone problem i.e. maximizing the number of
# correct answers given by the intelligent agent.
# Note the following during implementation:
# a. Number of questions: 10
# b. Population size: 15
# c. Selection operator: Roulette Wheel Selection
# d. Corrosover operator: Multi-point crossover having two crossover points
# e. Mutation operator: Bit Flip Mutation
# f. Crossover probability: 0.6
# g. Mutation probability:0.5
# h. Maximum number of generations: 30
# Report the solution quality and computational time.

import random
import time

NUM_QUESTIONS = 10
POPULATION_SIZE = 15
MAX_GENERATIONS = 30
CROSSOVER_PROB = 0.6
MUTATION_PROB = 0.


def generate_individual():
    return [random.randint(0, 1) for _ in range(NUM_QUESTIONS)]

def fitness(individual):
    return sum(individual)

def roulette_wheel_selection(population, fitness_values):
    total_fitness = sum(fitness_values)
    probabilities = [f / total_fitness for f in fitness_values]
    cumulative_probabilities = [sum(probabilities[:i+1]) for i in range(len(probabilities))]
    rand = random.random()
    for i, p in enumerate(cumulative_probabilities):
        if rand <= p:
            return population[i]
    return population[-1]

def crossover(parent1, parent2):
    crossover_points = sorted(random.sample(range(1, NUM_QUESTIONS), 2))
    child1 = parent1[:crossover_points[0]] + parent2[crossover_points[0]:crossover_points[1]] + parent1[crossover_points[1]:]
    child2 = parent2[:crossover_points[0]] + parent1[crossover_points[0]:crossover_points[1]] + parent2[crossover_points[1]:]
    return child1, child2

def mutate(individual):
    for i in range(len(individual)):
        if random.random() < MUTATION_PROB:
            individual[i] = 1 - individual[i]
    return individual

def genetic_algorithm():
    population = [generate_individual() for _ in range(POPULATION_SIZE)]
    start_time = time.time()

    for generation in range(MAX_GENERATIONS):
        fitness_values = [fitness(individual) for individual in population]
        best_individual = population[fitness_values.index(max(fitness_values))]
        best_fitness = max(fitness_values)

        print(f"Generation {generation+1}: Best fitness = {best_fitness}")

        new_population = []
        for _ in range(POPULATION_SIZE):
            parent1 = roulette_wheel_selection(population, fitness_values)
            parent2 = roulette_wheel_selection(population, fitness_values)
            if random.random() < CROSSOVER_PROB:
                child1, child2 = crossover(parent1, parent2)
                new_population.extend([child1, child2])
            else:
                new_population.extend([parent1, parent2])

        for i in range(len(new_population)):
            new_population[i] = mutate(new_population[i])

        population = new_population

    end_time = time.time()
    print(f"Solution quality: {best_fitness}")
    print(f"Computational time: {end_time - start_time:.2f} seconds")
    return best_individual

# Run the Genetic Algorithm
best_individual = genetic_algorithm()
print(f"Best individual: {best_individual}")
