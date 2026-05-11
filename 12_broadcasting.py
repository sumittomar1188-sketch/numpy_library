# brodcasting - ye karta he kis trh do difrrent dimensiion ke array me arithmetic operation operation perform ho jate he 
# isme agar ek he (3,4)ka matrix or ek (4) ka to isme (1,4) pehle esa banega fir (3,4) esa to easily operation hot jaega
import numpy as np 
a = np.arange(12).reshape(3,4)
b = np.arange(4).reshape(4)
print(a+b)

# rules of broadcasting 
# 1) - make the two array having same number of dimenssions 
    #  if the dimension of two array are diff then,add new dimmension with size 1 to the head of the array of smallest ones

# 2) - make each array of dimmension of ame size 
    #  if the size of both array does not match ,dimmension with size 1 are strecthed agar tab bhi equal nahi hua to 
    # error dega fir vo brodcast nahi hoga 
a = np.arange(15).reshape(3,5)
b = np.arange(4).reshape(2,2) # ab yha par error aaega kyuki 1 ke liye koi jgh hi nahi bachi he 
print(a+b)

