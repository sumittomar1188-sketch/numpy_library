import numpy as np 
a = np.random.randint(1,100,24).reshape(6,4)
b = np.append(a,np.ones((a.shape[0],1)),axis=1)
print(b)

a1  = np.arange(6).reshape(2,3)
b1 = np.arange(6,12).reshape(2,3)

# ye genertally stacking jesa he add kar deta he 
print(np.concatenate((a1,b1))) # vertical or horizontal adding karta he 
print(np.concatenate((a1,b1),axis=1))