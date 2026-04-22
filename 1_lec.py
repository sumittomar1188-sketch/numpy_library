import numpy as np
# 1D array or vector
a = np.array([1,2,3,4])
print(a)
print(type(a))

# 2D array and 3D array 
b = np.array([[1,2,3,4],[5,6,7,8]])
print(b) # matrix

c = np.array([[[1,2],[3,4]],[[1,4],[5,6]]])
print(c) # tenser
# by default ye float type ke rehte he 


# ========== dtype =================
# dtype = isse ham kisi bhi array ka type change kar sakte he 
d = np.array([2,3,4,3],dtype=float)
print(d)

# np.arange = it work like a range array bana dega ye 
print(np.arange(1,10))
print(np.arange(1,10,2)) 

# range with reshape 
# ye sape dega usko ki konse sphape me matrix banai he 
print(np.arange(1,13).reshape(6,2))


# np.ones - ye ek arrary crete kar deta he 1 values ka jo ki intinilize same value in neural network example 
print(np.ones((3,5)))
# np.zeros - this is for given or intitiallize same value 
print(np.zeros((3,4)))

# np.random - this is gives random values 
print(np.random.random((3,4)))


# np.linspace - ye space means point generate kar deta HE bich me array ke 
print(np.linspace(-10,10,9)) # -10 se 10 tak fir har equal parts ke bad 9 point banana

# np.identity - isse ham identity matrix bana sakte he 
print(np.identity((3)))