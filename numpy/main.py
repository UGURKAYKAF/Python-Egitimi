import numpy as np
import time 

arr = np.array([1, 2, 3, 4, 5])

arr_squared = arr ** 2
print(type(arr))
print(arr_squared)

# # *************************************************************************

initialTime = time.time()
revenues = [2000,5000,3000,6500,7200,3100,2650,1900,3820,5120,4100]
sum = 0
for i in revenues:
    sum +=i

print(sum)
terminationTime = time.time()

print("Execution Time: ", terminationTime - initialTime)

# *************************************************************************

revenues = [2000,5000,3000,6500,7200,3100,2650,1900,3820,5120,4100]
array = np.array(revenues)
initialTime = time.time()
sum = array.sum()
print(sum)
terminationTime = time.time()
print("Execution Time: ", terminationTime - initialTime)

# *************************************************************************

x = ["Ben", 500, "Jake", "liz", 6000]
print(x)

for i in x :
    print(type(i))

# *************************************************************************

array = np.array([[1,2,3],[4,5,6]])
print(array)

print(array.ndim)
print(array.shape)
print(array.size)