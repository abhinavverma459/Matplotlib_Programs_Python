# Multiple points
import matplotlib.pyplot as plt
import numpy as np

#Draw a line in a diagram form position(1,3) to (2,8) thern (6,1) & finally to position (8,10):
    
xpoints=np.array([1,2,6,8])
ypoints=np.array([3,8,1,10])

plt.plot(xpoints,ypoints)
plt.show()