# mathematical function we can calculate many regular built in diye hue he jese ki sum sin max bhot sare 
# ek concept he sigmoid jo ki ml me logical regression me use he 

# sigmoid formula - s(x) = 1/1+e power-x
# ab hamare pass iske liye koi built in function to he nahi to hame k kudka dunction banege 
import numpy as np 
def sigmoid (array):
    return 1/1+np.exp(-(array))

a = np.arange(100)
print(sigmoid(a))

# ml me ham both sare losses ke bare me padenge or usme pehla topic he logistic regression
# usme ek concept he mean square error
# mean square error - isme data me se jo sytem prdecit karta he galat usko - karke square karke mean nikalte he 
def mse(actual,predecit):
    return  np.mean((actual-predecit)**2)

actual = np.random.randint(1,100,24)
predecit= np.random.randint(1,100,24)

print(actual)
print(predecit)
print(mse(actual,predecit))

# binary cross entropy
# homework he 