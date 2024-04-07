# Implement stochastic hill climbing algorithm (considering probability of selection can
# vary with steepness of uphill move) for the following problem:
# Divide the N students in k groups based on their marks in the course AI such as
# diversity in each group is minimized (where, N=10 and k=3)

import random
import numpy as np

# Function to calculate diversity within a group
def calculate_diversity(group):
    return np.std(group)

# Function to generate a random neighbor
def generate_random_neighbor(groups):
    non_empty_groups = [i for i in range(len(groups)) if len(groups[i]) > 1]
    if len(non_empty_groups) < 2:
        return groups
    i, j = random.sample(non_empty_groups, 2)
    student = random.choice(groups[i])
    groups[i].remove(student)
    groups[j].append(student)
    return groups

# Stochastic hill climbing algorithm
def stochastic_hill_climbing(marks, k=3, max_iter=1000):
    groups = [list(x) for x in np.array_split(np.random.permutation(marks), k)]
    for _ in range(max_iter):
        neighbor = generate_random_neighbor(groups)
        delta = sum(calculate_diversity(group) for group in neighbor) - sum(calculate_diversity(group) for group in groups)
        if delta < 0 or random.random() < np.exp(-delta):
            groups = neighbor
    return groups


# Generate random marks for 10 students
marks = [random.randint(50, 100) for _ in range(10)]


# Apply the algorithm to group the students
groups = stochastic_hill_climbing(marks)

# Print the groups and their diversities
for i, group in enumerate(groups):
    print(f"Group {i+1}: {group}, Diversity: {calculate_diversity(group)}")


