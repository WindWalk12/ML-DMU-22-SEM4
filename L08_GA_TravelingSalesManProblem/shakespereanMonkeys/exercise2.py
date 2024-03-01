import random
import string


sentence = "To be or not to be that is the question"
def randomStringGen(str_size, allowed_chars, noOfStrings = 10000):
    strings = []
    for i in range(noOfStrings):
        strings.append(''.join(random.choice(allowed_chars) for x in range(str_size)))
    return strings


chars = string.ascii_letters + " "
size = 39

#print(chars)

strings = randomStringGen(size, chars)

def fitnessFunction(array):
    fitness = 0
    bestSentence = ""
    for i in range(len(array)):
        correct = 0
        for j in range(len(sentence)):
            if array[i][j] == sentence[j]:
                correct += 1
            if correct > fitness:
                fitness = correct
                bestSentence = array[i]
    return "Best sentence is: " + bestSentence + " with fitness " + str(fitness)

print(fitnessFunction(strings))