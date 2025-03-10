import matplotlib.pyplot as plt 
import numpy as np 



x = np.arange(0,50)
y1 = x**2
y2 = x**4


plt.figure(figsize=(5,5))
plt.title="Graphs with x to power of indicies"
plt.xlabel="x"
plt.ylabel="y"
plt.plot(x,y1,color="red",label="to power of 4")
plt.plot(x,y2,color="blue",label="to power of 9")
plt.legend()
plt.axis([0,100,0,200])
plt.show()
