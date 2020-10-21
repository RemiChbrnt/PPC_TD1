#!/bin/usr/env python3

from multiprocessing import Process
import os
import time


def childFib(name,nbTerms):
        print("DEBUG: Starting child")
        f0=0
        f1=1
        print(str(f0))
        print(str(f1))

        for j in range(nbTerms-1):
            print(str(f0+f1))
            store=f1
            f1+=f0
            f0=store
        print(str(os.getpid()))    
if __name__ == "__main__":
    print("Nothing to be Done")

print("DEBUG: Starting Parent")
ch = Process(target=childFib,args=("child1",10))
ch.start()
ch.join()
print(str(os.getpid()))
while True :
    if ch.is_alive(): 
        time.sleep(1000)
    else:
        break



