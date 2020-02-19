"""
#############################################################################################
# @author Tucker Ferguson                                                                   #
# @date 1/11/2020                                                                           #
# @descrip using the numpy library I will demonstrate several multi dimensional             #
# array calculations. (max,min,sum,axis=0,axis=1,vertical stack, horizontal stack           #
#############################################################################################
"""
import numpy as np

#Pre-defined shape checker
SHAPESIZE = (2,4,4)
dimension_check = False

sevensArray = np.array([
                        [[7,7,7,7],[7,7,7,7],[7,7,7,7],[7,7,7,7]],
                        [[7,7,7,7],[7,7,7,7],[7,7,7,7],[7,7,7,7]]
                       ])
                       
if(SHAPESIZE == sevensArray.shape):
    dimension_check = True

print("Initialized a 3D array of 7s:\n{0}\n\n".format(sevensArray))
print("The goal was to create:  2 x 4 x 4 array\nLets check!\nDoes: {0} == 2 x 4 x 4?? ({1})\n".format(sevensArray.shape,dimension_check))
print("\nNext lets add some variety to our array values\nand extract some data using numpy methods\n")

#By "adding variety I am simply adding an identical shaped array initialized with pseudo random values"
dudArray = np.array([
                    [[1,2,3,4],[4,3,2,1],[1,2,3,4],[4,3,2,1]],
                    [[3,2,1,0],[0,1,2,3],[4,3,2,1],[1,2,3,4]]
                    ])
ranArray = sevensArray + dudArray
print("Our new pseudo random array:\n\n{}".format(ranArray))
print("\nThe sum of all members is: {0}\nThe sum of the x axis is:\n{1}\n\nThe sum of the y axis is:\n{2}\n"
.format(ranArray.sum(),ranArray.sum(axis=0),ranArray.sum(axis=1)))
print("Next we concatenate two 3D-arrays using stacking:\n")

horizontalArray = np.hstack((sevensArray,dudArray))
vertArray = np.vstack((sevensArray,dudArray))
print("Vertical Stack:\n{}".format(vertArray))
print("\nHorizontal stack:\n{}".format(horizontalArray))



