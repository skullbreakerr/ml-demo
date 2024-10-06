import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

newArray = array.reshape(4,3)
print(newArray)

twodArray = array.reshape(3,4)

print(twodArray)

arr = np.random.randint(0,50,size=(6,6))
print()
print(arr)

ans = arr.reshape(6,2,3)  #reshape( no. of outerlist, no. of innerList , no. of Elements in each group)
                          
                          #reshape(total pair of matrix, no. of pairs(1D list), no. of elements in each list)

print(ans)
