import matplotlib.pyplot as plt

x_axis = '{}'.format(input("Enter in your x coordinates seperated by a ','\n>"))
y_axis = '{}'.format(input("Enter in your y coordinates seperated by a ','\n>"))
x_label = input("Enter in a label for the x axis\n>")
y_label = input("Enter in a label for the y axis\n>")

print(x_axis)
print(y_axis)

x_axis = x_axis.split(",") if x_axis != '' else [1,2,3,4]
y_axis = y_axis.split(",") if y_axis != '' else [1,4,9,16]

plt.plot(x_axis, y_axis)
plt.xlabel(x_label if x_label != '' else "x-axis")
plt.ylabel(y_label if y_label != '' else "y-axis")
plt.show()
