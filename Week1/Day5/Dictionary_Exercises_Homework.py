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

# Exercise 3 - Letter Summary 

# given_string = str.lower((input('Please submit a string: ')))
# def letter_count(given_string):
#     dict = {}
#     for n in given_string:
#         keys = dict.keys()
#         if n in keys:
#             dict[n] += 1
#         else:
#             dict[n] = 1
#     return dict

# print(letter_count(given_string))

# Exercise 4 - Word Summary
# given_string = str.lower((input('Please submit a string: ')))
# def word_count(given_string):
#     dict = {}
#     for word in given_string.split(' '):
#         if word  not in dict:
#             dict[word] = 1
#         else:
#             dict[word] += 1
#     return dict

# print(word_count(given_string))
