import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array(['Mon', 'Tues',' Wed', 'Thurs',' Fri'])
y = np.array([300,450,150,400,650])

plt.subplot(2, 1, 1)
plt.plot(x,y,ls = ':',color = 'c',marker = 'h',mfc = 'm',mec = 'k')
plt.grid()
plt.xlabel("Days of Week")
plt.ylabel("Sale of Drinks")
plt.title("Sales Data1",loc='right')

#plot 2:
x = np.array(['Mon','Tues',' Wed', 'Thurs',' Fri'])
y = np.array([400,500,350,300,500])

plt.subplot(2, 1, 2)
plt.xlabel("Days of Week")
plt.ylabel("Sale of Food")
plt.title("Sales Data2",loc='right')
plt.plot(x,y,ls = '-',color = 'y',marker = 'D',mfc = 'g',mec = 'r')
plt.grid()
plt.show()