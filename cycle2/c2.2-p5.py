import numpy as np
A = np.array([[6, 1, 1],
              [4, -2, 5],
              [2, 8, 7]])
  
inv=np.transpose(A)
neg=np.negative(A)
print ("Original Matrix\n",A)
print ("Traspose Matrix\n",inv)
print ("Negative Matrix\n",neg)
comparison = A == inv
comparison1 = inv== neg
equal_arrays = comparison.all()
skew=comparison1.all()
if equal_arrays :
    print("Given Matrix is Symmetric")
else:
    print("Given Matrix is not Symmetric")
    
if skew:
    print("Given Matrix is Skew Symmetric")
else:
    print("Given Matrix is Not Skew Symmetric")
    
        
    
    
    
