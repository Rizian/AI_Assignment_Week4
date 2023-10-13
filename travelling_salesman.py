import numpy as np
import random

class Route:
    def __init__(self, path_matrix, start_city, route = None):
        self.path_matrix = path_matrix
        self.num_cities = len(path_matrix)
        self.start_city = start_city
        if route is not None:
            self.route = route
        else:
            self.route = [start_city]
            remaining_cities = list(range(self.num_cities))
            remaining_cities.remove(start_city)
            self.route.extend(random.sample(remaining_cities, self.num_cities - 1))
        
    def fitness(self):
        total_distance = 0

        for i in range(self.num_cities - 1):
            from_city = self.route[i]
            to_city = self.route[i + 1]
            total_distance += self.path_matrix[from_city][to_city]

        total_distance += self.path_matrix[self.route[-1]][self.start_city]

        return total_distance

    def crossover(self, other):
        start = random.randint(0, self.num_cities - 1)
        end = random.randint(start, self.num_cities)

        selected = self.route[start:end]

        remaining = [city for city in other.route if city not in selected]

        new_route = remaining[:start] + selected + remaining[start:]

        return Route(self.path_matrix, self.start_city, new_route)

    def mutate(self):
        index1, index2 = random.sample(range(self.num_cities), 2)
        self.route[index1], self.route[index2] = self.route[index2], self.route[index1]

def genetic_algorithm(path_matrix, start_city, population_size, generations, mutation_rate):
    population = [Route(path_matrix, start_city) for _ in range(population_size)]

    for generation in range(generations):
        population = sorted(population, key=lambda route: route.fitness())
        new_population = population[:population_size // 2]

        while len(new_population) < population_size:
            parent1, parent2 = random.sample(population, 2)
            child = parent1.crossover(parent2)
            if random.random() < mutation_rate:
                child.mutate()

            new_population.append(child)

        population = new_population

    best_path = min(population, key=lambda route: route.fitness())

    return best_path

# random seeds for consistency (no specific reason for the numbers, I just mashed my keyboard)
np.random.seed(43274932)
random.seed(98346276)

# Weighted adjacency matrix of the graph
graph = np.array([
    [float('inf'), 12, 10, float('inf'), float('inf'), float('inf'), 12],
    [12, float('inf'), 8, 12, float('inf'), float('inf'), float('inf')],
    [10, 8, float('inf'), 11, 3, float('inf'), 9],
    [float('inf'), 12, 11, float('inf'), 11, 10, float('inf')],
    [float('inf'), float('inf'), 3, 11, float('inf'), 6, 7],
    [float('inf'), float('inf'), float('inf'), 10, 6, float('inf'), 9],
    [12, float('inf'), 9, float('inf'), 7, 9, float('inf')]
])

# Specifying the city we start at
start_city = 0

best_route = genetic_algorithm(graph, start_city, population_size=100, generations=1000, mutation_rate=0.1)

print("Best route:", best_route.route)
print("Best route distance:", best_route.fitness())