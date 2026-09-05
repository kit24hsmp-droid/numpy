import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
print(arr[1:5])



import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
print(arr[3:])


# 
import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
print(arr[:3])


# negative slicing
import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
print(arr[-5:-1])


#step slicing
import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
print(arr[1:8:2])

#slicing 2D array
import numpy as np
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[1,1:4]) # this is used to find the 2nd element on 1st dimension and 2nd to 5th element on 2nd dimension


