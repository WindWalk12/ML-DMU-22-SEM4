import pandas as pd
import math
import matplotlib.pyplot as plt
import itertools

data = pd.read_csv('TSPcities1000.txt',sep=r'\s+',header=None)
data = pd.DataFrame(data)
x = data[1]
y = data[2]


input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
all_permutations = itertools.permutations(input_list)

# calculate distance between cities
def distance_between_cities(city1x, city1y, city2x, city2y):
    xDistance = abs(city1x-city2x)
    yDistance = abs(city1y-city2y)
    distance = math.sqrt((xDistance * xDistance) + (yDistance * yDistance))
    return distance


def fitness_function(route):
    fitness = 0
    for j in range(len(route) - 1):
        fitness += distance_between_cities(x[route[j]], y[route[j]], x[route[j + 1]], y[route[j + 1]])
    return fitness


def plot_city_route(route):
    x_coords_route = [x[i] for i in route]
    y_coords_route = [y[i] for i in route]
    plt.plot(x_coords_route, y_coords_route, marker='o', linestyle='-')
    plt.title('Route Plot')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()


def brute_force_tsp():
    min_distance = float('inf')
    best_path = None
    for perm in all_permutations:
        d = fitness_function(perm)
        if d < min_distance:
            min_distance = d
            best_path = perm
            print("Best: " + str(min_distance))
    print("Best path: " + " ".join(str(e) for e in best_path) + " With distance: " + str(min_distance))
    plot_city_route(best_path)


brute_force_tsp()
