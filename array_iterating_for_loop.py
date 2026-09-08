import numpy as np 
arr = np.array([1,2,3,4,5])
for x in arr:
    print(x) # this is used to iterate through the array using for loop 
    
    
    
# iterating 2d array 
import numpy as np
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
for x in arr:
    print(x) # this is used to iterate through the 2d array using for loop
    
    
# iterating in each sclar value of 2d array
import numpy as np
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
for x in arr:
    for y in x:
        print(y) # this is used to iterate through each scalar value of 2d array using for loop
        
        
# 3d array
import numpy as np
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for x in arr:
    print(x) # this is used to iterate through the 3d array using for loop
    
    
#iterating in each scalar value of 3d array
import numpy as np 
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for x in arr:
    for y in x:
        for z in y:
            pritn(z) # this is used to iterate through each scalar value of 3d array using for loop
