##########################################################
# UPDATED CODE PREVIOUS WAS BROKEN SO SORRY!!!!!!!!!!!!! #
##########################################################
#                      - ALLAN -                         #
##########################################################
import math
import random
import time
start = time.time()
layers = 5
width = 4
Vasic = 10000

def roll():
    return(random.choice([0,-1]))
def start():
    return(random.randint(1,width))
# 0 1 2 3
#  0 1 2 
# 0 1 2 3
def even(a,length):
    rolld = roll()
    a += rolld
    if(a<0 or a>(length-1)):
      if(a >length-1):
        return(length-2)
      else:
        return(0)
    else:
        return(a)
def odd(number):
  rolled = roll()
  number+=(rolled+1)
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
