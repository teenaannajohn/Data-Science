import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Walking", "Cycling", "Car", "bus","Train"])
y = np.array([29, 15, 35, 18,3])
plt.title("Mode of Transport")
plt.xlabel("Mode of Transport")
plt.ylabel("frequency")
plt.bar(x, y, width = 0.1,color="g")
plt.show()