import matplotlib.pyplot as plt
import numpy as np

y = np.array([1, 9, 20, 30, 40])

mylabels = ["Sleep", "Homework", "Procrastination", "Reading", "School"]
mycolors = ["blue", "purple", "red", "yellow", "green"]
myexplode = [0,0,0,0,0]
plt.pie(y, explode = myexplode, colors = mycolors, labels = mylabels, autopct='%.1f%%', startangle = 0,wedgeprops = {"edgecolor" : "white",'linewidth': 2,'antialiased': True})
plt.title("Time spent in a day")
plt.show()