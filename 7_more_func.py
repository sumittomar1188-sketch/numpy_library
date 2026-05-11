 # reshape - we already know about it 
# troanspose(T) - transpose 3x4 matrix into 
import numpy as np 
a = np.arange(12).reshape(3,4)
print(a)
print(np.transpose(a))
print(a.T)



# ravel - 2d ko 1d me conver kar deta he 
print(np.ravel(a))