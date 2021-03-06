import time
import random 
from os import system
import platform
width=80
height=30
size=(width*height)
world1=list("0"*(size+1))
world2=world1.copy()
cls="cls" if platform.system()=="Windows" else "clear"

# Calculate a new generation..
def Generation(now,new):
    for i in range(width,size-width):
        if i % width==0: print("")
        t=int(now[i-1]) + int(now[i+1]) + int(now[i-width]) + int(now[i+width]) + int(now[i-width+1]) + int(now[i-width-1]) + int(now[i+width-1]) + int(now[i+width+1])
        if now[i]=="0":
            print(" ",end='')
            new[i]="1" if t==3 else "0"
        else:
            print("O",end='')
            new[i]="0" if (t<2 or t>3) else "1"

# Initialise random world...
for i in range(width,size-width):
        if random.randrange(0,7)==1: world1[i]="1"

# Main Loop
while True:
    system(cls)
    Generation(world1,world2)
    time.sleep(.1)
    system(cls)
    Generation(world2,world1)    
    time.sleep(.1)    
