import numpy as np
a1 = np.arange(12).reshape(3,4)
a2 = np.arange(1,31).reshape(5,2,3)
print(a2)
print(a1)
print('')
print('')

# min /max /sum /prod
print(np.max(a1,axis=1)) # row
print(np.max(a1,axis=0)) # column
print(np.prod(a1))
print(np.sum(a1))



# mean/meadian /std - standard deviation / Var 
print(np.mean(a1))
print(np.var(a2,axis=0))


# trgmomentry 
print(np.sin(a1))
print(np.sin(90)) 

# dot product / exponent
a = np.arange(10).reshape(2,5)
b = np.arange(11,21).reshape(5,2)
print(np.dot(a,b))

# round /flor /ceil
# lets do it with random example 
a = (np.random.random((2,3))*100) #- it gives us random number hundred tak koi sa bhi 
# round - round off kar dega nearest integer par 
print(np.round(np.random.random((2,3))*100))

# flor - ye pichhe wale integer par chala jaega
print(np.floor(np.random.random((2,3))*100))

# ceil - ye next integer par jump karega mean ki point me andwer nahi aaega
print(np.ceil(np.random.random((2,3))*100))  