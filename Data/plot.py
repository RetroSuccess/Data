from matplotlib import pyplot as plt

x = [1,2,3,4,5]
y = [8,10,12,14,16]

colors = ["blue", "green", "orange", "yellow", "red"]
plt.bar(x, y, color=colors)

plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("A plot")
plt.show()
