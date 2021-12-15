import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([2001,2002,2003,2004,2005,2006, 2007])
ypoints = np.array([24000, 22500,19700,17500,14500,10000,5800])

plt.title("Value Depreciation",loc='left')
plt.xlabel("Year")
plt.ylabel("Car Value")
plt.plot(xpoints, ypoints,marker = '*', ms = 20, mfc = 'g',ls = '-.',color = 'r')
plt.show()