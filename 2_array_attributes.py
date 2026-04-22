import numpy as np 
a1 = np.arange(10)
a2 = np.arange(12,dtype=int).reshape(3,4)
a3 = np.arange(16).reshape(2,2,2,2)
print(a1)
print(a2)


# ndim - dimension btata he 
print(a1.ndim)
print(a2.ndim)
print(a3.ndim)


# shape - shape bata he (3,3) or (4,4)
print(a1.shape)
print(a2.shape)
print(a3.shape)

# size - kitne items he array me v bata ta he 
print(a1.size)
print(a2.size)
print(a3.size)

# itemsize - ye item size bata ta he ki each elemnet ne kitna size liya he memory me
print(a1.itemsize)
print(a2.itemsize)
print(a3.itemsize)
a2.astype(np.int32)

# dtype - ye type bata deta he array ka  lets take an example
print(a1.dtype) # just like it 
 
# atype - isme ham jab memory ko chhota karke use karna ho to int64 se int32 me change kar sakte he jisse memory kam use hogi 