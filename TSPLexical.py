import numpy as np
import matplotlib.pyplot as plt 
import random
import math
from matplotlib.animation import FuncAnimation
distance = 0
bestDistance = math.inf
counter = 0
def lexicalOrder(a):
    larXInd = 0
    larX = -1
    larYInd = 0
    larY = -1
    for i in range (len(a)-1):
        if a[i]<a[i+1] :
            larX = a[i]
            larXInd = i

    for j in range (len(a)):
        if a[j]>a[larXInd] :
            larYInd = j
            larY = a[j]
    
    if larX !=-1 and larY != -1:
        a[larXInd] = larY
        a[larYInd] = larX
        a[larXInd+1:len(a)]= reversed(a[larXInd+1:len(a)])
    print(a)
    return a

def getDistance(sol):
    d = 0
    for i in range(len(sol)-1):
        d+=(x[sol[i]]-x[sol[i+1]])**2+(y[sol[i]]-y[sol[i+1]])**2
    d+=(x[sol[-1]]+x[sol[0]])**2+(y[sol[-1]]-y[sol[0]])**2
    return d

def update_plot(b):
    plt.clf()
    global bestDistance
    global distance
    global best
    global counter
    global n
    if counter < math.factorial(n):
        swaped=lexicalOrder(sol)  
        distance = getDistance(swaped)
        print(bestDistance)
        print(counter)
        if distance < bestDistance:
            bestDistance = distance
            best = sol.copy()
        counter+=1
    done = str(round(((counter/math.factorial(n))*100),2))+"% finished"
    plt.scatter(x,y, color='red')
    for i in range(len(sol)-1):
        plt.plot((x[sol[i]],x[sol[i+1]]),(y[sol[i]],y[sol[i+1]]),color='blue')
    plt.plot((x[sol[-1]],x[sol[0]]),(y[sol[-1]],y[sol[0]]),color='blue')
    plt.scatter(xBest,yBest, color='red')
    for i in range(len(best)-1):
        plt.plot((x[best[i]],x[best[i+1]]),(y[best[i]]+20,y[best[i+1]]+20),color='pink')
    plt.plot((x[best[-1]],x[best[0]]),(y[best[-1]]+20,y[best[0]]+20),color='pink')
    plt.title(done)
    plt.xlim(0,41)
    plt.ylim(0,41)

n = 8
dots = []
bestDots=[]
start = (random.randint(1,10),random.randint(1,10))
x =[]
y=[]
sol = []
best = []
xBest = []
yBest = []

for i in range(n):
    a = random.randint(1,40)
    b = random.randint(1,20)
    x.append(a)
    y.append(b)
    xBest.append(a)
    yBest.append(b+20)
    dots.append((x,y))
    sol.append(i)
fig=plt.figure()
anim = FuncAnimation(fig,update_plot,frames=10,interval = 100,)
plt.show()



