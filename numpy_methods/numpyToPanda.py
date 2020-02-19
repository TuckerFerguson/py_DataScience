#@author Tucker Ferguson
#1/18/2020
#Formatting numpy array using pandas DataFrames()

import numpy as np  
import pandas as pd 
import pdb;

np_Array = np.array([["","col1","col2"],["row1","01","10"],["row2","11","00"]])

print("{}  ...Ugly right?\n\n".format(np_Array))

np_Dataframe = pd.DataFrame(data = np_Array[1:,1:],index = np_Array[1:,0],columns = np_Array[0,1:])
#pdb.set_trace()

print("{}   ...Pandas makes it pretty!".format(np_Dataframe))
