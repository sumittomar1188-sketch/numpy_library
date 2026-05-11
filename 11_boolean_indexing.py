
import numpy as np 
a = np.random.randint(1,100,24).reshape(6,4)
print(a)
# yha to random item 24 print karega 1 s 24 tak 
# lekin apan ko isme se chatna pade ki 50 se kam batao konse he to vha boolean indexing ka use karenge 
print(a[a<50]) # ab yha vahi elemnt print honge jo ki 50 se chhote honge

# print divisible by 5
print(a[a%5==0])

print(a[~a%7==0])

# do condition me & ka use karenge rasther than and 

import numpy as np 
a = np.random.randint(1,100,24).reshape(6,4)
print(a)
# yha to random item 24 print karega 1 s 24 tak 
# lekin apan ko isme se chatna pade ki 50 se kam batao konse he to vha boolean indexing ka use karenge 
print(a[a<50]) # ab yha vahi elemnt print honge jo ki 50 se chhote honge

# print divisible by 5
print(a[a%5==0])

print(a[~a%7==0])

# do condition me & ka use karenge rasther than and 

