import numpy as np
import matplotlib.pyplot as mnp
x = np.linspace(-10,10,100)
y = x+2
mnp.plot(x,y)
mnp.show()


# parabola
x = np.linspace(-10,10,100)
y = x**2
mnp.plot(x,y)
mnp.show()

# sinx

x = np.linspace(-10,10,100)
y = np.sin(x)
mnp.plot(x,y)
mnp.show()

# xlogx
x = np.linspace(-10,10,100)
y = x*np.log(x)
mnp.plot(x,y)
mnp.show()

# sigmoid 
x = np.linspace(-10,10,100)
y = 1/(1+(np.exp(-x)))
mnp.plot(x,y)
mnp.show()