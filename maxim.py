import math
import fastrand
import random
import time
start = time.time()
layers = 5
width = 10
Vasic = 1000000

def roll():
    return(random.choice([1,-1]))
def start():
    return(fastrand.pcg32bounded(width)) #0123
    
def even(number,length):
    rolld = roll()
    number += rolld
    if(number not in range(length)):
        number = number + (rolld*-1*2)
        return(number)
    else:
        return(number)
def odd(number):
    number = number + roll()

    return(number)

def maxim():
    
    position = start()
    for x in range(layers):
        if (x%2==0):
            position = even(position,width)
        else:
            position = odd(position)
    return((position))
data=[]
for x in range(Vasic):
    do = maxim()
    data.append(do)
    if(x%10000==0):
        print(str(x))
from collections import Counter
for x in range(width):
    #print(Counter(data)[x])
    print((Counter(data)[x]/Vasic)*100)

with open("thedata5.txt", "w+") as file:
    for datayes in data:
        file.write(str(datayes) + "\n")
print(str(time.time()-start)+" seconds")    
    
