#
# @author Tucker Ferguson
# 1/10/2020
#
# @Descrip Numpy Versus Lists (memory usage and speed)

import time
import sys
import numpy as np

#Arbitrary Large Size
SIZE = 1000000

"""
This is the total memory usage comparison between python list and numpy array

Here we will test it with 100 elements

"""
#The list will use up more memory due to the nature in which it stores items
listNew = range(100)
memoryUsed = sys.getsizeof(4) * len(listNew) 
print("The list used up {} bytes\n".format(memoryUsed))

#The numpy array uses up less memory due to all items being same type, etc.
numpyNew = np.arange(100)
memoryUsed = numpyNew.size * numpyNew.itemsize
print("The numpy array used up {} bytes\n".format(memoryUsed))

print("*********************************************************")

"""
Below is the speed comparison between python lists and numpy arrays
"""

#List should take longer to iterate
LA = range(SIZE)
LB = range(SIZE)
startTime = time.time()
[(x,y) for x,y in zip(LA,LB)]
totalTime = time.time() - startTime
totalTime = round(totalTime,2)
print("Total time for List {} sec\n ".format(totalTime))


#Numpy array takes less sytem time to iterate
PA = np.arange(SIZE)
PB = np.arange(SIZE)
start = time.time()
PA + PB
totalTime = time.time() - start
totalTime = round(totalTime,3)
print("Total time for Numpy Array {} sec".format(totalTime))
