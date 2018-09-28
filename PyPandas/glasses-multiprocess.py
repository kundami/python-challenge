#!/usr/bin/env python

import numpy as np
from multiprocessing import Process, Queue
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())


def brothersInTheBar(glasses,q):
    gulgp=True
    info('function brothersInTheBar')
    count=0
    a_glass = np.array(glasses)
    i=0
    N = len(a_glass)
    while i < N:
        #print("here"+str(len(a_glass)) + str(i))
        if (i+2) <N and a_glass[i] == a_glass[i+1] and a_glass[i] == a_glass[i+2]:
            #x = np.array([i,i+1,i+2])
            a_glass=np.delete(a_glass,np.array([i,i+1,i+2]))
            N=len(a_glass)
            #print(a_glass)
            count=count+1
            i=0
        else:
            i=i+1
            continue
    print(count)
    q.put([count,a_glass])
    return count

if __name__ == '__main__': 
    info('main line')
    print("start")
    #glasses=np.random.randint(low=1, high=100, size=1000)
    glasses=[12978, 15535, 15535, 15535, 20517, 20517, 20517, 12978, 12978, 20517, 32604, 37094, 37094, 45241, 45241, 45241, 37094, 32604, 32604, 45241, 53861, 53861, 53861, 61067, 61067, 62521, 62521, 62521, 61067, 62521, 71919, 71919, 75322, 79189, 79189, 79189, 75322, 75322, 71919, 79189, 87326, 88379, 88379, 92690, 92690, 92690, 88379, 87326, 87326, 92690, 100099, 102042, 103883, 103883, 103883, 102042, 102042, 100099, 100099, 103883, 117484, 117484, 117484, 125467, 125467, 125467, 127006, 127006, 127006, 127006, 135556, 141537, 141537, 147526, 147526, 147526, 141537, 135556, 135556, 147526, 161186, 161186, 163852, 163852, 163852, 161186, 165269, 165269, 165269, 165269, 177657, 178552, 185823, 185823, 185823, 178552, 178552, 177657, 177657, 185823]
    print("before split")
    q = Queue()
    x = [0,0,0]
    sum = 0
    final = []
    x[0], x[1], x[2] = np.array_split(glasses,3)
    Process_jobs = []
    print("A"+str(len(x)))
    for i in range(0,len(x)):
    	p = Process(target=brothersInTheBar, args=(x[i],q))
    	Process_jobs.append(p)
    	#p.daemon=True
    	p.start()
    	p.join()
    	a,b = q.get()
    	sum = sum + a
    	#print(str(sum))
    	if b.any():
    		final = np.concatenate((final,b),axis=None)
    		#print(b)
    #print(final)		
    brothersInTheBar(final,q)
    a,b = q.get()
    sum = sum+a 
    print("x:"+str(b)+"c:"+str(sum))
