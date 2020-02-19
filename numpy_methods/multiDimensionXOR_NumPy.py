"""
@author Tucker Ferguson
1/9/2020

Simulating 'XOR' on a 3D array, using the numpy library (array,shape,ones)

"""

import numpy as np

#3D array to preform 'XOR' operation on 
my3dArray = np.array([
                    [[0,1,0],
                        [0,1,0],
                            [0,1,0]],
                     [[0,1,0],
                        [0,1,0],
                            [0,1,0]],
                    [[0,1,0],
                        [0,1,0],
                            [0,1,0]]
                    ])
                    
#Get the shape of the array to be inverted 'my3dArray'
shape = my3dArray.shape

#Next create an equal in dimensions array of integer values: 1 'onesArray'
onesArray = np.ones(shape,int)


#Using the logic below we effectively invert the array it can also be seen as an Xor
copyArray = my3dArray
my3dArray = (my3dArray - onesArray) * -1
print("{0}\n\n XOR \n\n{1}\n\n Equals \n\n{2}".format(copyArray,onesArray,my3dArray))