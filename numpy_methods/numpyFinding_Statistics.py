import numpy as np  
import pdb

my_np = np.array([[4,3,2,3],
                  [5,4,3,1]])

x_sum = my_np.sum(axis=0)
y_sum = my_np.sum(axis=1)

print("Sum of axis 0: {}\nSum of axis 1: {}\n".format(x_sum,y_sum))

dimensions = np.shape(my_np)

xLen,yLen = dimensions[1],dimensions[0]

for x in np.nditer(my_np):
    print(x)

x_total = my_np.cumsum(axis=0)
print(x_total)

breakpoint()

x_total = x_total[len(x_total)-1]
y_total = my_np.cumsum(axis=1)

#x_average = my_np.total(axis=0)

#y_average = y_sum / yLen


print("first off success on break pointsteppin\n")

breakpoint()

print("done")






