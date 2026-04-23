import numpy as np 

a1 = np.arange(10) 
a2 = np.arange(1,13).reshape(3,4)
a3 = np.arange(27).reshape(3,3,3)
print(a1)
print(a1[1:5])
print(a1[::-1])


print(a2)
print(a2[2,1]) # row , column
print(a2[1,:]) # isse row print ho jaega
print(a2[1:,1:3])
# corner ke elments lelo sare 
print(a2[::2,::3])
print(a2[::2,1::2])
print(a2[1,::3])
print(a2[:2,1::])



print(a3)
print(a3[2,1:,1:])
print(a3[::2,0,::2])