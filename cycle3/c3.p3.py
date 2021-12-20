#Three lines to make our compiler able to draw:

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
plt.title("Sales Data")
plt.xlabel("Months of Year",size=18)
plt.ylabel("Sales of Segments")
#day one, the age and speed of 13 cars:
x = np.array(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
y = np.array([173,153,195,147,120,144,148,109,174,130,172,131])
plt.scatter(x, y,color = 'hotpink')

#day two, the age and speed of 15 cars:
x = np.array(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
y = np.array([189,189,105,112,173,109,151,197,174,145,177,161])
plt.scatter(x, y,color = 'y')

#day two, the age and speed of 15 cars:
x = np.array(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
y = np.array([185,185,126,134,196,153,112,133,200,145,167,110])
plt.scatter(x, y,color = 'b')

plt.show()


