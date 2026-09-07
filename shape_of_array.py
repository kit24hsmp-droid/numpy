import numpy as np 
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr.shape) # this is used to find the shape of the array


# ndim
import numpy as np
arr = np.array([1,2,3,4,5],ndmin=5)
print(arr)
print('number of dimensions:', arr.ndim) # this is used to find the number of dimensions of the array