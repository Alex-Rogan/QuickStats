import matplotlib.pyplot as plt
import numpy as np
xpoints=np.array([1,2,6,8])
ypoints=np.array([3,8,1,10])

plt.plot(xpoints,'o--r')
plt.plot(ypoints,'o-b')
plt.title("Stupid Plot")
plt.xlabel("Dumb Axis")
plt.ylabel("Ridiculous Axis")
plt.grid(color='green', linestyle='-', linewidth=0.25)
plt.show()
