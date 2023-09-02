import matplotlib.pyplot as plt
import numpy as np

# draw two points in the diagram , onw at position (1,3) & one in position (8,10):
    
xpoints=np.array([0,6])
ypoints=np.array([0,250])

plt.plot(xpoints,ypoints,'o')
plt.show()