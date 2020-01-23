import matplotlib.pyplot as plt
import numpy as np

def yx(x, x1, y1, x2, y2):
    return ((y2-y1)*(x-x1)/(x2-x1)+y1)

def function ():
    n = list(map(int, input('Enter the number of points on the graph: ').split()))
    n[0] -= 1
    coord = list(map(int, input('Enter the coordinates of the x, y points through a space: ').split()))

    dx = 0.1

    xg = []
    xg = np.arange(coord[0], coord[2+2*(n[0]-1)]+dx, dx)
    yg = []

    for i in range(0, n[0]-1):
        print (i)
        x = []
        x = np.arange(coord[0+2*i], coord[2+2*i], dx)
        y = yx(x, coord[0+2*i], coord[1+2*i], coord[2+2*i], coord[3+2*i])
        yg.extend(y)

    x = []
    x = np.arange(coord[0 + 2 * (n[0]-1)], coord[2 + 2 * (n[0]-1)]+dx, dx)
    y = yx(x, coord[0 + 2 * (n[0]-1)], coord[1 + 2 * (n[0]-1)], coord[2 + 2 * (n[0]-1)], coord[3 + 2 * (n[0]-1)])
    yg.extend(y)
    return xg, yg

x1, y1 = function()
x2, y2 = function()
x3, y3 = function()

y4 = [0] * len(x1)
y5 = [0] * len(x1)

for i in range(len(x1)):
    y4[i] = max(y1[i], y2[i], y3[i])
    y5[i] = min(y1[i], y2[i], y3[i])

fig, ax = plt.subplots()
ax.plot(x1, y1, linewidth=4, color="blue", label="y1(x)")
ax.plot(x2, y2, linewidth=4, color="red", label="y2(x)")
ax.plot(x3, y3, linewidth=4, color="green", label="y3(x)")
ax.plot(x1, y4, linestyle='-.', color="white", label="ymax(x)")
ax.plot(x1, y5, linestyle='-.', color="yellow", label="ymin(x)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
plt.show()
fig.savefig('1.png')