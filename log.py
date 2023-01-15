import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [2, 4, 6, 5, 6, 8]
y2 = [5, 3, 7, 8, 9, 6]

fig, ax = plt.subplots()

ax.plot(x, y)
ax.plot(x, y2)
plt.show()