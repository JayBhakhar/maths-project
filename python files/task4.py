import matplotlib.pyplot as plt
import numpy as np

a1 = int(input("enter x1 :- "))
a2 = int(input("enter y1 :- "))
b1 = int(input("enter x2 :- "))
b2 = int(input("enter y2 :- "))

x1 = [a1,b1]
y1 = [a2,b2]


def line1(x, x1, y1, x2, y2):
    return ((y2-y1)*x/(x2-x1)-(y2-y1)*x1/(x2-x1)+y1)

if a1<b1:
    x = np.arange(a1,b1,0.1)
else:
    x = np.arange(b1,a1,0.1)
y = line1(x, a1, a2, b1, b2)
plt.plot(x,y)
plt.show()
