# Day 4 - Functions
# f(x) = mx + b  (Used to transform inputs to outputs)


# def samplefunc():
#     print ("Hello World")

# samplefunc() # This here is what is called "calling" a function

# def f(x):
#     print (x)

# f("Hello World") # "Calls" function "f"
# f("Digital Crafts") # Code is reusable
# f(19) # Code is reusable

#Example 1
# def f(x):
#     return x * x

# myFunctionCall = f(4) # Return populates this variable
# print (myFunctionCall) # Call the variable to be printed

#Example 2
# def f(x):
#     return x * x
# def g(x):
#     return x + 1

# for index in range(-3, 5):
#     print("f({x})={y} \t g({x})={z}").format(x=index, y=f(index), z=g(index))
#Recheck example 2 for error**

# Example 3

# def f(x):
#     return 2 * x + 1
# print (f(2))

# def g(x):
#     return x + 1
# print (g(2))

# print (g(f(2)))

# Example 4
# def f(x):
#     return 2 * x + 1

# def g(x):
#     return x + 1

# for x in range (-3, 5):
#     print ("f({x}) = {y}".format(x=x, y= f(x))) #formatting function replaces context within the print statement

# Example 5
# def samplefunction(a, b, c):
#     print ("{a} {b} {c}".format(a=a, b=b, c=c))

# samplefunction(1, 2, 3) # to reorganize arguments, samplefunction (c=3, a=2, b=1) will work but it has to be stated

#Example 6 - Quadratic Equations
# from math import sqrt
# def quadratic(a, b, c):
#     x1 = -b / (2*a)
#     x2 = sqrt(b**2 - 4*a*c) / (2*a)
#     return (x1 + x2), (x1 - x2)

# print (quadratic(31, 93, 62))

# Additional Notes - Global versus Local Variables
#   Global Variable - variable declared outside of a function
#   Local Variable - variable declared within a function (scope is constrained)

#Example 7 
# a = 5 # This is an example of a Global Variable
# def practice():
#     a = 3 # This is an example of a Local Variable
#     print(("inside function: {a}").format (a=a))

# print(("outside function: {a}").format (a=a))
# practice() # must call the function for it to print "inside function"

# Example 8
# a =[1, 2, 3, 4, 5]

# def someFunction():
#     newArray = a.copy() #make a copy to ensure that old list does not change, this is an independent copy
#     newArray[0] = 234
#     print(newArray)

# someFunction()
# print (a)

# Plotting Example

# import matplotlib
# matplotlib.use("Agg")
# from matplotlib import pyplot

# xrange = list(range(2, 10))
# yrange = list(range(2, 10))

# pyplot.plot(xrange, yrange) # Plot Function

# pyplot.savefig('samplePlot.png') # SaveFig Function

# pyplot.close() # Close Function

# Plot Example 2 utilize pip3 install matplotlib prior to running python3 [filename]

# f_output = []
# g_output = []

# x_list = list(range(-3, 5))

# def f(x):
#     return 2 * x + 1

# def g(x):
#     return x + 1

# for x in x_list:
#     f_output.append(f(x))
#     g_output.append(g(x))

# pyplot.plot(x_list, f_output, x_list, g_output)

# pyplot.savefig('new.png')
# pyplot.close() # start a new plot


#List 1 multiplied and sum by List 2 into List 3 Example

# def determinant(list1, list2, list3):

#     for indexList1 in list1 :

#         list3SummedValue = 0
#     print("list 1 index: {}".format(indexList1))
#     for indexList2 in list2:
#         list3SummedValue += indexList1 * indexList2
#         print("accumulatedValue {}".format(list3SummedValue))

#     list3.append(list3SummedValue)

#     print(list3)

# v1r = ''
# v1 = []
# print ('vector 1 values: to end type done')
# while (v1r != 'done'):
#     if (v1r != 'done'):
#         v1.append(int(input(">>")))

# print(v1)


# list1 = [1,5,3,6,7]
# list2 = [3,6,9,10,2]
# list3 = []
# print(determinant(list1, list2, list3))


# Turtle Graphics Example

# from turtle import *
# for i in range(5):
#     forward(100)
#     right(144)
# mainloop()