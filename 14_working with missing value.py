# working with missing value - np.nan - means yha missing value he 
import numpy as np
a = np.array([1,2,3,4,np.nan,5])
# ab ham missing value ke sath deal karenge
print(np.isnan(a))
print(a[~np.isnan(a)])