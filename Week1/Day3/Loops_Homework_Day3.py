# 1. 1 to 10
# for numbers in range (1,11):
#     print (numbers)

# 2. n to m
# start_input = int(input("Please enter the number the range should start on "))
# stop_input = int(input("Please enter the number the range should stop on "))

# for numbers in range (start_input, stop_input):
#     print (numbers)

# 3. Odd Numbers
# for numbers in range (0,10):
#     if numbers % 2 != 0:
#         print(numbers)

# 4. Print a Square
# size = 5
# for square in range(size):
#     print ( "*" * size)

# 5. Print a Square II
# user_question = int(input("How large of a square would you like? Enter a number between 0 and 10. "))
# size = user_question
# if 0 <= size <= 10:
#     for x in range(size):
#         print ( "*" * size)
# else:
#     print("Please try again!")

# 6. Print a Box

# height = int(input("Provide a number between 1 - 20 for the height of the box. "))
# width = int(input("Provide a number between 1 - 20 for the width of the box. "))

# space = " "

# def box (height,width):
#     for x in range(height):
#         if x == int(0) or x == int(height-1):
#             print (width*'*')
#         else:
#             print ('*' + space*(width-2) + '*')
# print (box(height,width))

# 7. Print a Triangle
# height = 4
# for i in range(height):
#     print (' ' * (height - i - 1) + "*" * (2 * i + 1))

# 8. Print a Triangle II
# height = int(input('How yall do you want the triangle? '))
# for i in range(height):
#         print(' ' * (height - i - 1) + "*" * (2 * i + 1))

# 9. Multiplication Table
# for outerindex in range (1,11):
#     # print ("Index:", index)
#     for innerindex in range (1, 11):
#         print ((outerindex), " x ", innerindex, " = ", (outerindex * innerindex))
