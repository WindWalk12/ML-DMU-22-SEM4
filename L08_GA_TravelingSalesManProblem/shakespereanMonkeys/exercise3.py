import random
import string


sentence = "To be or not to be that is the question"
def randomStringGen(str_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for x in range(str_size))


chars = string.ascii_lowercase + " "
size = 39

#print(chars)

randomString = randomStringGen(size, chars)

def fitnessFunction(randomString):
    fitness = 0
    for i in range(len(randomString)):
        correct = 0
        if randomString[i] == sentence[i]:
            correct += 1
        if correct > fitness:
            fitness = correct
    return fitness

def hillClimbing(randomString):
    fitness = 0
    bestSentence = randomString
    print(bestSentence)
    i = 0
    while fitness <= size:
        i = i + 1
        rand = random.randint(0, 38)
        sentencelist = list(bestSentence)
        sentencelist[rand] = random.choice(chars)
        tempSentence = "".join(sentencelist)
        tempFitness = fitnessFunction(tempSentence)
        if tempFitness > fitness:
            fitness = tempFitness
            bestSentence = tempSentence
        if i % 1000 == 0:
            print("Best sentence right now is: " + bestSentence + " with fitness: " + str(fitness))
    print("Done: " + bestSentence + " with fitness: " + str(fitness))


hillClimbing(randomString)