import numpy as np 
a = np.random.randint(1,100,24).reshape(6,4)
print(a)
b = np.sort(a)
print(b) # row wise by default
print(np.sort(a,axis=0)) # column wise sorting 




