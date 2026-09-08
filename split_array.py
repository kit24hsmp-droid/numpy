import numpy as np 
arr = np.array([[1,2,3,4,5,6]])
newarr = np.array.split(arr,3)# this is used to split the array into 3 parts
print(newarr)
               

# splitting array into 4 parts 
import numpy as np 
arr = np.array([[1,2,3,4,5,6]])
newarr = np.array.split(arr,4)# this is used to split the array into 3 parts
print(newarr)


# return value 
import numpy as np
arr = np.array([[1,2,3,4,5,6]])
newarr = np.array_split(arr,3) # this is used to split the array into
print(newarr[0]) # this is used to print the first part of the array
print(newarr[1]) # this is used to print the second part of the array
print(newarr[2]) # this is used to print the third part of the array


#split 2d array into 3 2d arrays
import numpy as np

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)

print(newarr)