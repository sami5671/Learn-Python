import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

y = [2, 4, 6, 8, 10, 12, 14, 16, 18, 19, 20, 21, 22, 23, 24, 25]

plt.plot(x, y)
plt.xlabel('X Axis level')
plt.ylabel('Y Axis level')
plt.title("Simple Level")

plt.savefig('line.jpg', format="png")
# plt.show()