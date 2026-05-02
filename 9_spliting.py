# isme bhi do type se hota he horizontal split and vertical split 
import numpy as np 
a1 = np.arange(12).reshape(3,4)
a2 = np.arange(12,24).reshape(3,4)

print(a1)
print(np.hsplit(a1,2))
print(np.vsplit(a2,3))
