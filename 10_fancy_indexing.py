
# fancy indexing - jab koi pattern nahi ban pata he tab ye use hota he 
import numpy as np
# isme list ke andar batate he ki konsa elemnt chahiye 
a =np.arange(1,25).reshape(4,6) 
print(a)
print(a[[1,2]])
# column ke liye
print(a[:,[1,2]])