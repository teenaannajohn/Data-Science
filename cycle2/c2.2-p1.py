import numpy as np
from numpy import random
x=random.randint(100, size=(3,3))
inv = np.linalg.inv(x) 
print("Matrix:\n",x)
print("Inverse:\n",inv)
rank=np.linalg.matrix_rank(x)
print("Rank:",rank)
print ("Determinant:",np.linalg.det(x))
arr = x.flatten()
print("Matrix to array:\n",arr)
w, v = np.linalg.eig(x)
print("Eigen value:\n",w)
print("Eigen Vector:\n",v)