import random
import string


sentence = "To be or not to be that is the question"
def randomStringGen(str_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for x in range(str_size))


chars = string.ascii_letters + " "
size = 39

#print(chars)

randomString = randomStringGen(size, chars)

def fitnessFunction(randomString):
    fitness = 0
    correct = 0
    for i in range(len(randomString)):
        if randomString[i] == sentence[i]:
            correct += 1
    if correct > fitness:
        fitness = correct
    return fitness

def hillClimbing(randomString):
    fitness = 0
    bestSentence = randomString
    i = 0
    while fitness < size:
        i += 1
        rand = random.randint(0, 38)
        sentencelist = list(bestSentence)
        sentencelist[rand] = random.choice(chars)
        tempSentence = "".join(sentencelist)
        tempFitness = fitnessFunction(tempSentence)
        if tempFitness > fitness:
            fitness = tempFitness
            bestSentence = tempSentence
        if i % 1000 == 0:
            print("i: " + str(i) + " Best sentence right now is: " + bestSentence + " with fitness: " + str(fitness))
    print("i: " + str(i) + " Done: " + bestSentence + " with fitness: " + str(fitness))

hillClimbing(randomString)