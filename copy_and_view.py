# copy changs 
import numpy as np
arr = np.array([1,2,3,4,5])
x = arr.copy() # this is used to create a copy of the array
arr[0] = 10 # this is used to change the value of the first element of the array
print(arr)
print(x) # this is used to print the copy of the array


# view changes
import numpy as np
arr = np.array([1,2,3,4,5])
x = arr.view() # this is used to create a view of the array 
arr[0] = 10 # this is used to change the value of the first element of the array
print(arr)
print(x) # this is used to print the view of the array



# using copy and view 
import numpy as np 
arr = np.array([1,2,3,4,5])
x = arr.copy() # this is used to create a copy of the array
y = arr.view() # this is used to create a view of the array
arr[0] =10
print(x.base) # this is used to print the base of the copy of the array
print(y.base) # this is used to print the base of the view of the array
