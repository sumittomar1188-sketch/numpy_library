import numpy as np 
a1 = np.arange(10) 
a2 = np.arange(1,13).reshape(3,4)
a3 = np.arange(27).reshape(3,3,3)

# 1D array me to sare element ek ek karke print ho jate he 
for i in a1:
    print(i)

# but 2D array me ek row ko execute arega loop 
for i in a2 :
    print(i)


# or 3D me to ek single 2d ARRAy ko execute karega 
for i in a3 :
    print(i)



# to solve this we can use np.nditer
for i in np.nditer(a3) :
    print(i)   
 