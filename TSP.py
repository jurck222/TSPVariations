import numpy as np
import matplotlib.pyplot as plt 
import random
import math
from matplotlib.animation import FuncAnimation
distance = 0
bestDistance = math.inf

   

def swap(sol,a,b):
    temp = sol[a]
    sol[a]=sol[b]
    sol[b]=temp
    return sol

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
    ran1 = random.randint(0,n-1)
    ran2 = random.randint(0,n-1)
    swaped=swap(sol,ran1,ran2)  
    distance = getDistance(swaped)
    print(bestDistance)
    if distance < bestDistance:
        bestDistance = distance
        best = sol.copy()
    
    plt.scatter(x,y, color='red')
    for i in range(len(sol)-1):
        plt.plot((x[sol[i]],x[sol[i+1]]),(y[sol[i]],y[sol[i+1]]),color='blue')
    plt.plot((x[sol[-1]],x[sol[0]]),(y[sol[-1]],y[sol[0]]),color='blue')
    for i in range(len(best)-1):
        plt.plot((x[best[i]]+10,x[best[i+1]]+10),(y[best[i]]+10,y[best[i+1]]+10),color='pink')
    plt.plot((x[best[-1]]+10,x[best[0]]+10),(y[best[-1]]+10,y[best[0]]+10),color='pink')
    plt.xlim(0,21)
    plt.ylim(0,21)

n = 6
dots = []
bestDots=[]
start = (random.randint(1,10),random.randint(1,10))
x =[]
y=[]
sol = []
best = []


for i in range(n):
    x.append(random.randint(1,10))
    y.append(random.randint(1,10))
    dots.append((x,y))
    sol.append(i)
fig=plt.figure()
anim = FuncAnimation(fig,update_plot,frames=10,interval = 500,)
plt.show()



