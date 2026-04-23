# array creation 
import numpy as np 
a1 = np.arange(12).reshape(3,4)
a2 = np.arange(12,24).reshape(3,4)
print(a1)
print(a2)

# array operation
# scalar operation - jo sirf ek single array par operation lagae 
# Arithemtic operations 
a = a1*2
print(a)
a = a1+2
print(a)

# relational operations
a = a1>5 # if ture to print true or false to print flase 
print(a)

# vector operations - means jab do arrays apas me operate karte he 
a = a1*a2
print(a)
a = a1+a2
print(a)



