# Dictionary Exercises 

# Exercise 1
# phonebook_dict = {
#     'Alice': '703-493-1834',
#     'Bob': '857-384-1234',
#     'Elizabeth': '484-584-2923'
# }

# Print Elizabeth
# print (phonebook_dict['Elizabeth'])

# Add Kareem
# phonebook_dict['Kareem'] = '968-345-2345'
# print(phonebook_dict)

# Delete Alice's phone entry
# del phonebook_dict['Alice']
# print(phonebook_dict)

# Change Bob's phone Number
# phonebook_dict['Bob'] = '968-345-2345'
# print(phonebook_dict)

# Print all the phone entries
# print(phonebook_dict)

# Exercise 2: Nested Dictionaries
# ramit = { 
#   'name': 'Ramit', 
#   'email': 'ramit@gmail.com', 
#   'interests': ['movies', 'tennis'], 
#   'friends': [ 
#      { 
#        'name': 'Jasmine', 
#        'email': 'jasmine@yahoo.com', 
#        'interests': ['photography', 'tennis']
#      }, 
#      { 
#         'name': 'Jan', 
#         'email': 'jan@hotmail.com', 
#         'interests': ['movies', 'tv'] 
#      } 
#     ] 
# }

# Exercise 2 (#1)
# print (ramit['email'])

# Exercise 2 (#2)
# print (ramit['interests'][0])

# Exercise 2 (#3)
# print(ramit['friends'][0]['email'])

# Exercise 2 (#4)
# print(ramit['friends'][0]['interests'][1])

# Exercise 3 - Letter Summary - Need to revisit!!

# letter_dictionary = {
#     "a" : 0,
#     "b" : 0,
#     "c" : 0,
#     "d" : 0,
#     "e" : 0,
#     "f" : 0,
#     "g" : 0,
#     "h" : 0,
#     "i" : 0,
#     "j" : 0,
#     "k" : 0,
#     "l" : 0,
#     "m" : 0,
#     "n" : 0,
#     "o" : 0,
#     "p" : 0,
#     "q" : 0,
#     "r" : 0,
#     "s" : 0,
#     "t" : 0,
#     "u" : 0,
#     "v" : 0,
#     "w" : 0,
#     "x" : 0,
#     "y" : 0,
#     "z" : 0
# }

# question_list = []
# question = str.lower(input('Enter a word to receive a tally of each letter: '))
# question_list.append(question)

# def letter_histogram(question):
#     for x in range(len(question_list)):
#         if x == "a":
#            question_list["a"] = "a" + 1

# letter_histogram(question)
# print (question_list)

