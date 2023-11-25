#Write a Numpy program to create a 3x3 matrix with values ranging from 2 to 10.

#Importing the Numpy module as np
import numpy as np

#Creating the 3*3 matrix and shaping the matrix with 3 rows and 3 columns and the elements of the matrix range from 2 to 10
A=np.arange(2,11).reshape(3,3)

#Printing the outputs
print(A)

#Output
#[[ 2  3  4]
 #[ 5  6  7]
 #[ 8  9 10]]
