import numpy as np 
a = np.arange(12).reshape(3,4)
b = np.array([2,3,3,2,33,22,11,87])

#  ========= np.put =========
# ye put kardega array me or replace kar dega new value denge position sahit to 
np.put(b,[0,1],[100,101]) # ye isme  original array me permanent changes kar dega
print(b)
print(np.delete(b,0)) #  isme se delted ho jaega 
print(b) # par isme rahega



# selts function are also applicable here 
print(np.union1d(a,b)) # ye to union bataega 
print(np.intersect1d(a,b)) # ye vahi intersection 
np.setdiff1d(a,b)
np.setxor1d(a,b)

# special one np.in1d = check karega ki 1d me he ki nahi vo item jo apan denge 
m = np.array([4,5,3,5,3,5,3,5])
print(np.isin(m,5))

# ========== np.clip ===========
# ye ek range me band dega ki isse niche to ye item dedo as output 
print(np.clip(a,a_max=20,a_min=2))