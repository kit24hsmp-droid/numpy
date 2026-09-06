import numpy as np
arr = np.array([1,2,3,4,5])
print(arr.dtype) # this is used to find the data type of the array

#string data type
import numpy as np

arr = np.array(['apple', 'banana', 'cherry'])

print(arr.dtype)

# now int to string 
import numpy as np
arr = np.array([1,2,3,4,5], dtype='S')
print(arr)

#float to intiger
import numpy as np

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype(int)

print(newarr)
print(newarr.dtype)

#bool to intiger
import numpy as np

arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)