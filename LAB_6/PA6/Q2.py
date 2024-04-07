import random
import math

def tsp_objective(cities, tour):
    return sum(cities[tour[i-1]][tour[i]] for i in range(len(tour)))

def random_neighbor(tour):
    i, j = random.sample(xrange(len(tour)), 2)
    neighbor = tour[:]
    neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
    return neighbor


def simulated_annealing(cities, temp=1000, cooling_rate=0.995, max_iter=1000):
    tour = cities.keys()
    random.shuffle(tour)

    for _ in range(max_iter):

        neighbor = random_neighbor(tour)

        delta = tsp_objective(cities, neighbor) - tsp_objective(cities, tour)

        if delta < 0 or random.random() < math.exp(-delta / temp):
            tour = neighbor

        temp *= cooling_rate

    return tour, tsp_objective(cities, tour)

cities = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
}

for _ in range(5):
    temp = random.uniform(500, 1500)
    cooling_rate = random.uniform(0.9, 0.999)
    max_iter = random.randint(500, 1500)
    tour, tour_length = simulated_annealing(cities, temp, cooling_rate, max_iter)
    print "Initial temperature: %s, Cooling rate: %s, Number of iterations: %s, Shortest tour: %s, Tour length: %s" % (temp, cooling_rate, max_iter, tour, tour_length)
