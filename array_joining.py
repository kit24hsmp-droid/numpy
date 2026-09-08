import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.concatenate((arr1,arr2)) # this is used to join two arrays
print(arr) # this is used to print the joined array

# joining 2d arrays
import numpy as np
arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])
arr = np.concatenate((arr1,arr2),axis=0) # this is used to join two 2d arrays along the first axis
print(arr) # this is used to print the joined 2d array



