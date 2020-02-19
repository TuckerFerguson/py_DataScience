#find min and max of a flattened array
import numpy as np 

my_Array = np.array([
    [[1,3,2,5],[1,2,4,3]],
    [[3,2,1,4],[4,3,1,2]]
    ])

my_Array = my_Array.flatten()
print("Max: {}\n".format(max(my_Array)))
print("Min: {}".format(min(my_Array)))