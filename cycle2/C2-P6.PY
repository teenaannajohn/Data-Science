import numpy as np
a = np.array([[1, 2, 3,4], [4, 5, 6,5], [7, 8, 9,6], [10, 11, 12,7]])
print(a)
print("elements excluding the first row:\n",a[1:])
print("elements excluding the first Column:\n",a[:,:3])
print("elements of 2 nd and 3 rd column:\n",a[:,1:3])
print("2 nd and 3 rd element of 1 st row:",a[0,1],a[0,2])

