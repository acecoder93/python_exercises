# File I/O = File Input Output

# Read a File
# file_handle = open('lorem.txt', 'r') # "r" stands for read
# contents = file_handle.read() #lorem  ipsum is a dummy file that programmers used
# file_handle.close() # This closes off the open connection

# print (contents)

# Write a File
# file_handle = open('newFileTest.txt', 'w') # "w" stands for write
# contents = file_handle.write("HERE IS NEW CONTENT!!") #lorem  ipsum is a dummy file that programmers used
# file_handle.close() # This closes off the open connection

# Read it Again - Retreive code from Veronica's GITHUB
# file_handle = open('lorem.txt', 'r')
# contents = file_handle.readline()
# file_handle.close()
# print(contents)

# Read it Again and Again - this block of code needs to be fixed because it continuously runs
# file_handle = open('lorem.txt', 'r')
# while True: # keep on executing this block of code until you hit a break
#     char = file_handle.read(1)
#     if char is None:
#         break # Usually, when while loops are used with "True", a break is utilized
#     else:
#         print (char)
# file_handle.close()

# Append to a File
# file_handle = open('lorem.txt', 'a') # 'a' stands for append
# file_handle.write('Hello World\n')
# file_handle.close()

# in Alternate Modes, 'rb' and 'wb' are used.
# 'rb' means read binary
# 'wb' means write binary

# Pickling: Saving Objects # Pickle allows you to create and save a dictionary to refer to later within a program
# import pickle
# data = {'name' : 'Paul'} # <- This here is the dictionary
# with open('data.pickle', 'wb') as fh: #This file handle will dump data 
#     pickle.dump(data, fh) # pickle.dump is the function
# # if you open this file, it will be a huge file as it has been stored as a binary file

# # Pickling: Loading Objects
# import pickle
# with open('data.pickle', 'rb') as fh:
#     data = pickle.load(fh) # The print out here should be the data that was saved in the previous block of code
#     print (data)

#JSON - JavaScript Object Notation - used to save contents into a file and load it
# json file can be opened up
# all of these commands here are standard documentation
# import json
# data = {'name' : 'Paul'}
# with open('data.json', 'w') as fh:
#     json.dump(data, fh) # "fh" stands for file handler    

# with open('data.json', 'r') as fh:
#     data = json.load(fh)
#     print(data)