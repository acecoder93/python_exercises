# Error and Debugging Notes

# Error Handling:
# while True: # a condition will be tested here
#     try:
#         x = int(input('Please enter a number: '))
#         break # This will sent x to False
#     except ValueError: # Value Error is a type of exception, make sure to include what kind of error if it is specific
#         print('Oops! That was no valid number. Try again...')
# print ('Goodbye')

# Advanced Methods
try:
    number = int(input('Enter number: '))
    result = number/0
except ValueError:
    print('enter in a number')
except ZeroDivisionError:
    print('Can\'t divide by zero')
except:
    print ('something bad happened')
finally: # usually used for cleaning up 
    print ('Closing Statement')