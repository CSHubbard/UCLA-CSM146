import numpy as np
import matplotlib.pyplot as plt
mean=0
#covmtx = np.mat("1 .5; .5 1")
xone = np.random.normal(mean,1,size=1000)
xtwo = np.random.normal(mean,1,size=1000)
randos = np.column_stack((xone,xtwo))
print(randos)
plt.scatter(xone,xtwo)
plt.show()