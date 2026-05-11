import numpy as np

# unique array me se unique alag kar dega 
a = np.array([1,2,1,2,1,2,3,4,3,4,5,6,6,5])
print(np.unique(a))

# ================== expand_dims ====================
# expand_dims - ye dimenssion bada deta he 1d-2D , 2D- 3D ese lets take an example axis batana padta he bss 
a = np.array([1,2,3,4,5,6,7,8,9,12,32,15,17])
print(np.shape(a))
a1 = np.expand_dims(a,axis=0)
print(a1) # ab iska shape 1,15 ho gya he row,column
a1 = np.expand_dims(a,axis=1)
print(a1) # ab axis change karne par vo 

# ============= where =======================
# NP.WHERE - index postion batat he jab condtion satisfy ho 
# meand ki a array me se 6 se bade number batana he konse index par he 
print(np.where(a>6)) # yha usne index numbe batA diye 
# ab hame iski jgh kuchh or replace karna he to isme ye hota he condtion true false 
# where(condition ,true-agr true he to kisse change karna he  ,false- he to kisse change karna he  )
print(np.where(a>20,0,a))
print(np.where(a>20,np.random.randint(1,10),a))

# ================ argmax ===================
# argmax - kisi bhi array se max index postion one line of code me bata dega 
print(np.argmax(a)) # index postion bata dega 

# =============== np.cumsum =================
# cumsum - cumulative sum aage aate aate pichhe wale se sum karna 
print(np.cumsum(a))  # isme 2 ki jgh 3 aaega or ese hi pichhe wala sabme add hota jaega
# isko 2d me bhi apply kar sakte he bass agar axis nahi di to 1d me change karke output dega 
b = np.arange(12).reshape(3,4)
print(np.cumsum(b))
print(np.cumsum(b,axis=0)) # column wise hua
print(np.cumsum(b,axis=1)) # row wise hua


# ============= np.cumprod ================
# cumprod - cumulative product isme addition ki jgh multiplication hota he 
print(np.cumprod(a))

# ============ np.percentile =============
# percentile - ye jese ki percntile me hota he to 100 percentile to sabse jyda max vese hi man lo 
print(np.percentile(a,100))
print(np.percentile(a,50))


# ============ np.histogram ===========
# ye frequency bta deta he bss graph plot nahi karta he 
print(np.histogram(a,bins=[1,10,20,30,40]))



# ============ np.corrcoef ===========
# corrcoef - correlation coffecient means ki ek ke badne par dusre par kya effect aata he
salary = np.array([2000,3000,5000,10000])
experinece = np.array([1,3,2,4])
print(np.corrcoef(salary,experinece))


#============ isin ==============
#np.isin = ye bhot kam ka function he vo bata he ki multiple item given array me he ki nahi 
items = [1,2,3,4,5,5]
print(np.isin(a,items))


#============ flip ==============
# flip - flip kar dega vo pure array ko 
print(np.flip(a))
# row or cloum wise flip ho jati he 2d me 

# ============= put =========
# np.put = putting new item on existing list 
