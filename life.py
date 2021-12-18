import time
import random
from os import system
system('cls')
worldnow=list("0"*1897)
worldnew=list("0"*1897)

for i in range(80,1816):
        if random.randrange(0,7)==1: worldnow[i]="1"

while 1:
        system('cls')
        for i in range(80,1816):
                if worldnow[i]=="1":
                        print("O",end='')
                else:
                        print(" ",end='')
                if i % 80==0: print("")
                t=int(worldnow[i-1]) + int(worldnow[i+1]) + int(worldnow[i-80]) + int(worldnow[i+80]) + int(worldnow[i-81]) + int(worldnow[i-79]) + int(worldnow[i+79]) + int(worldnow[i+81])
                if worldnow[i]=="0":
                        if t==3:
                                worldnew[i]="1"
                        else:
                                worldnew[i]="0"
                else:
                        if (t<2 or t>3):
                                worldnew[i]="0"
                        else:
                                worldnew[i]="1"
        time.sleep(.1)
        system('cls')
        for i in range(80,1816):
                if worldnew[i]=="1":
                        print("O",end='')
                else:
                        print(" ",end='')
                if i % 80==0: print("")
                t=int(worldnew[i-1]) + int(worldnew[i+1]) + int(worldnew[i-80]) + int(worldnew[i+80]) + int(worldnew[i-81]) + int(worldnew[i-79]) + int(worldnew[i+79]) + int(worldnew[i+81])
                if worldnew[i]=="0":
                        if t==3:
                                worldnow[i]="1"
                        else:
                                worldnow[i]="0"
                else:
                        if (t<2 or t>3):
                                worldnow[i]="0"
                        else:
                                worldnow[i]="1"
        time.sleep(.1)
