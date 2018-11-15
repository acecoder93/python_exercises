# 1. Hello
# def hello(name):
#     print('Hello ' + name)
# hello('Anuj')

# 2. y = x + 1
# import matplotlib.pyplot as pyplot

# def f(x):
#     return x + 1

# xrange = list(range(-3, 3))
# yrange = []

# for x in xrange:
#     yrange.append(f(x))

# pyplot.plot(xrange,yrange)
# pyplot.savefig('Homework2.png')
# pyplot.close()

# 3. Square of x
# import matplotlib.pyplot as pyplot

# def f(x):
#     return x**2

# xrange = list(range(-100,100,1))
# yrange = []

# for x in xrange:
#     yrange.append(f(x))

# pyplot.plot(xrange,yrange)
# pyplot.savefig('Homework3.png')
# pyplot.close()

# 4. Odd or Even
# import matplotlib.pyplot as pyplot
# def f(x):
#     if x % 2 == 0:
#         return 1
#     else:
#         return -1

# xrange = list(range(-5, 5, 1))
# yrange = []

# for x in xrange:
#     yrange.append(f(x))

# pyplot.bar(xrange,yrange)
# pyplot.savefig('Homework3.png')
# pyplot.close()

# 5. Sine
# import matplotlib.pyplot as pyplot
# from math import sin

# def f(x):
#     return sin(x)

# xrange = list(range(-5, 5))
# yrange = []


# for x in xrange:
#     yrange.append(f(x))

# pyplot.plot(xrange, yrange)
# pyplot.savefig('Homework4.png')
# pyplot.close() 

# 6. Sine 2
# import matplotlib.pyplot as pyplot
# from math import sin
# from numpy import arange

# def f(x):
#     return sin(x)

# xrange = list(arange(-5, 6, 0.1))
# yrange = []

# for x in xrange:
#     yrange.append(f(x))

# pyplot.plot(xrange, yrange)
# pyplot.savefig('Homework5.png')
# pyplot.close()

# 7. Degree Conversion
# import matplotlib.pyplot as pyplot
# from math import sin

# def f(x):
#     return x * 1.8 + 32

# xrange =  list(range(-10,10,1))
# yrange = []

# for x in xrange:
#     yrange.append(f(x))

# pyplot.plot(xrange, yrange)
# pyplot.savefig('Homework7.png')
# pyplot.close()

# 8. Play again?
# def playagain(x):
#     if x == "Y":
#         return "True"
#     elif x == "N":
#         return "False"
#     else:
#         print("Invalid")

# question = str.upper(input('Do you want to play again? (Y or N) '))
# print(playagain(question))

# 9. Play again? Again.
# question = str.upper(input('Do you want to play again? (Y or N) '))

# def playgame(x):
#     question = str.upper(input('Do you want to play again? (Y or N) '))
#     if x == "Y":
#         return ("True")
#     elif x == "N":
#         return ("False")
#     elif x != "N" and x != "Y":
#         while str.upper(question) != "Y" and str.upper(question) != "N":
#             question = str.upper(input('Do you want to play again? (Y or N) '))
#             print ("Invalid Input")
# print(playgame(question))