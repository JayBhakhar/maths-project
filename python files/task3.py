import matplotlib.pyplot as plt
# line 1 points
x1 = [1,2,4,5,6]
y1 = [1,4,4,2,6]
# plotting the line 1 points
plt.plot(x1, y1, label = "line 1",color='green', linewidth = 3,
         marker='o', markerfacecolor='yellow', markersize=12)

#line 2 points
x2 = [1,2,3,4,5,6]
y2 = [4,2,8,2,4,4]
# plotting the line 2 points
plt.plot(x2, y2, label = "line 2",color='red', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=12)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
# giving a title to my graph
plt.title('Two lines on same graph!')

# show a legend on the plot
plt.legend()

# function to show the plot

# plt.plot(min(x1,x2),max(y1,y2),label = "line 3",color="orange")
plt.show()
print(min(x1,x2),max(y1,y2))
