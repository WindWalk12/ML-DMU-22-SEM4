import random
import string

sentence = "To be or not to be that is the question"


def random_string_gen(str_size, allowed_chars, no_of_strings):
    strings = []
    for i in range(no_of_strings):
        strings.append([''.join(random.choice(allowed_chars) for x in range(str_size)), 0])
    return strings


# String settings
chars = string.ascii_letters + " "
size = 39

# Generation settings
population_size = 100
mutation_factor = 0.1
population_gen = 0


def fitness_function(population):
    for i in range(len(population)):
        fitness = population[i][1]
        correct = 0
        for j in range(len(sentence)):
            if population[i][0][j] == sentence[j]:
                correct += 1
            if correct > fitness:
                population[i][1] = correct


def generate_population(population_size):
    population_list = random_string_gen(size, chars, population_size)
    return population_list


def mutate(child):
    rand = random.randint(0, 38)
    sentence_list = list(child[0])
    sentence_list[rand] = random.choice(chars)
    child[0] = "".join(sentence_list)


def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2


def launch_population(population_size):
    global population_gen
    population = generate_population(population_size)
    while True:
        population_gen += 1
        fitness_function(population)
        population.sort(key=lambda x: x[1], reverse=True)
        fittest = population[0]
        if fittest[1] == size:
            print("On gen: " + str(population_gen) + " - Done: - " + fittest[0] + " - with fitness: " + str(fittest[1]))
            break
        new_population = [fittest]
        for i in range(len(population) // 2):
            parent1, parent2 = random.choices(population, k=2)
            child1, child2 = crossover(parent1, parent2)
            if random.random() < mutation_factor:
                mutate(child1)
            if random.random() < mutation_factor:
                mutate(child2)
            new_population.extend([child1, child2])
        population = new_population[:-1]
        print("Going to gen: " + str(population_gen) + " best fitness: " + str(fittest[1]))


launch_population(population_size)
