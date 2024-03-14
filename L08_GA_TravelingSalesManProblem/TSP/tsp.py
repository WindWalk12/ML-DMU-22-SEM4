import pandas as pd
import random
import math
import matplotlib.pyplot as plt

data = pd.read_csv('TSPcities1000.txt',sep=r'\s+',header=None)
data = pd.DataFrame(data)
x = data[1]
y = data[2]

# Generation settings
population_size = 100
mutation_factor = 0.7
population_gen = 0
route_size = 10  # Up to 1000


def create_random_route(route_size):
    tour = [i for i in range(route_size)]
    random.shuffle(tour)
    return tour


def generate_population(population_size):
    population_list = []
    for i in range(population_size):
        population_list.append([create_random_route(route_size), 0])
    return population_list


# calculate distance between cities
def distance_between_cities(city1x, city1y, city2x, city2y):
    xDistance = abs(city1x-city2x)
    yDistance = abs(city1y-city2y)
    distance = math.sqrt((xDistance * xDistance) + (yDistance * yDistance))
    return distance


def mutate(child):
    if random.random() < 0.5:
        rand_swap = random.randint(0, len(child[0]) - 2)
        temp_city = child[0][rand_swap]
        child[0][rand_swap] = child[0][rand_swap + 1]
        child[0][rand_swap + 1] = temp_city
    else:
        start_index = random.randint(0, len(child[0]) - 2)
        end_index = random.randint(start_index + 1, len(child[0]) - 1)
        while start_index < end_index:
            temp_city = child[0][start_index]
            child[0][start_index] = child[0][end_index]
            child[0][end_index] = temp_city
            start_index += 1
            end_index -= 1


def crossover(parent1, parent2):
    rand = random.randint(1, len(parent1[0]) - 1)
    child = [parent1[0][:rand], 0]
    for i in range(len(parent2[0])):
        if not parent2[0][i] in child[0]:
            child[0].append(parent2[0][i])
    return child


def fitness_function(population):
    for i in range(len(population)):
        fitness = 0
        for j in range(len(population[i][0]) - 1):
            fitness += distance_between_cities(x[population[i][0][j]], y[population[i][0][j]], x[population[i][0][j + 1]], y[population[i][0][j + 1]])
        population[i][1] = fitness


def plot_city_route(route):
    x_coords_route = [x[i] for i in route]
    y_coords_route = [y[i] for i in route]
    plt.plot(x_coords_route, y_coords_route, marker='o', linestyle='-')
    plt.title('Route Plot')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()


def launch_population(population_size):
    global population_gen
    population = generate_population(population_size)
    while True:
        population_gen += 1
        fitness_function(population)
        population.sort(key=lambda x: x[1])
        fittest = population[0]
        if population_gen == 10000:
            print("Done on gen: " + str(population_gen) + " - with best distance: " + str(fittest[1]) + " - Tour: " + " ".join(str(e) for e in fittest[0]))
            plot_city_route(fittest[0])
            break
        new_population = [fittest]
        for i in range(len(population) - 1):
            parent1, parent2 = random.choices(population, k=2)
            child = crossover(parent1, parent2)
            if random.random() < mutation_factor:
                mutate(child)
            new_population.extend([child])
        population = new_population
        if population_gen % 100 == 0:
            print("Going to gen: " + str(population_gen) + " with best distance: " + str(fittest[1]))


launch_population(population_size)
