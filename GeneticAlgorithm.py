import numpy as np
import matplotlib.pyplot as plt 
import random
from matplotlib.animation import FuncAnimation

def generatePopulation(sol, num):
    pop =[] 
    sez = []
    sez = sol.copy()
    for i in range(num):
        random.shuffle(sez)
        pop.append(sez.copy())
    return pop
    
def getDistance(sol):
    d = 0
    for i in range(len(sol)-1):
        d+=np.sqrt((x[sol[i]]-x[sol[i+1]])**2+(y[sol[i]]-y[sol[i+1]])**2)
    d+=(x[sol[-1]]+x[sol[0]])**2+(y[sol[-1]]-y[sol[0]])**2
    return d

def generateFitness(population):
    fitness = []
    for i in population:
        fit = 1.0/getDistance(i)
        fitness.append(fit)
    return fitness

def normalizeFitness(fitness):
    sum = 0
    for i in range(len(fitness)):
        sum+=fitness[i]
    for i in range(len(fitness)):
        fitness[i] = fitness[i]/sum
    return fitness

def selection(population,fitness):
    selected = []
    for i in range(2):
        r = random.random()
        sumProb = 0
        for i in range(len(population)):
            if r > sumProb and r < sumProb+fitness[i]:
                selected.append(population[i])
                break
            sumProb +=fitness[i]
    return selected

def crossover(population, fitness):
    cross = selection(population,fitness)
    parent1 = cross[0]
    parent2 = cross[1]
    child = [-1 for i in range(n)]
    child[0] = parent1[0]
    index = 0
    while True:
        index = parent1.index(parent2[index])       
        child[index] = parent1[index]
        if parent1[index] == parent1[0]:
            break
    for i in range(len(parent2)):
        if parent2[i] not in child:
            child[i] = parent2[i]
    return mutate(child)

def mutate(child):
    if random.randint(0,100) < 2:
       rin1 = random.randint(0,len(child)-1)  
       rin2 = random.randint(0,len(child)-1)       
       temp = child[rin1]
       child[rin1] = child[rin2]
       child[rin2] = temp
    return child     
    
def getBestInd(fitness):
    bestFitness = 0
    bestInd = 0
    for i in range(len(fitness)):
        if fitness[i]>bestFitness:
            bestFitness = fitness[i]
            bestInd = i
    return bestInd

def nextGen(population, popSize, fitness):
    newPop = []
    for i in range(popSize):
        newPop.append(crossover(population,fitness))
    return newPop

def geneticAlgorithm(pointList, popSize, generations):
    population = generatePopulation(pointList,popSize)
    fitness = generateFitness(population)
    fitness = normalizeFitness(fitness)
    for i in range(generations):
        population = nextGen(population, popSize, fitness)
        fitness = generateFitness(population)
        fitness = normalizeFitness(fitness)
    routeInd = getBestInd(fitness)
    return population[routeInd]

n = 8
dots = []
x =[]
y=[]
sol = []

for i in range(n):
    a = random.randint(1,40)
    b = random.randint(1,40)
    x.append(a)
    y.append(b)
    sol.append(i)

bestRoute = geneticAlgorithm(sol,300,600)
fig=plt.figure()
plt.scatter(x,y, color='red')
for i in range(len(bestRoute)-1):
    plt.plot((x[bestRoute[i]],x[bestRoute[i+1]]),(y[bestRoute[i]],y[bestRoute[i+1]]),color='blue')
plt.plot((x[bestRoute[-1]],x[bestRoute[0]]),(y[bestRoute[-1]],y[bestRoute[0]]),color='blue')
plt.show()

