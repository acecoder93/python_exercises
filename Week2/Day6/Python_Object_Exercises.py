# Python Object Exercises
# 1. Basics
# class Person: 
#     def __init__(self, name, email, phone, friends=None, greeting_count=None): 
#      self.name = name 
#      self.email = email 
#      self.phone = phone 
#     #  if friends is None:
#      friends = []
#      self.friends = friends
#      self.greeting_count = 0

#     def greet(self, other_person): 
#      print('Hello {}, I am {}!'.format(other_person.name, self.name))
#      self.greeting_count += 1
#      print ('Guess Count: {}'.format(self.greeting_count))

#     def print_contact_info(self):
#         print('{}\'s email: {}, {}\'s phone number {}'.format(self.name, self.email, self.name, self.phone))
    
#     def add_friend(self,new_friend):
#         self.friends.append(new_friend.name)
#         return self.friends
#         # print (self.friends)
    
#     def num_friends(self):
#         print (len(self.friends))
#         return self.friends

#     def __str__(self):
#         return 'Person: {} {} {}'.format(self.name, self.email,self.phone)

#     def num_unique_people_greeted(self):
#         num


# Jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')
# Sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')

# print(len(Sonny.friends))
# Sonny.greet(Jordan)
# Jordan.greet(Sonny)

# print (Sonny.name)
# print (Sonny.email)
# print (Sonny.phone)

# print (Jordan.name)
# print (Jordan.email)
# print (Jordan.phone)

# Sonny.print_contact_info()
# Jordan.print_contact_info()


# Sonny.friends.append(Jordan)
# Jordan.friends.append(Sonny)

# print(len(Sonny.friends))
# print(len(Jordan.friends))

# print (Jordan.add_friend(Sonny))
# print (Jordan.num_friends())

# Sonny.greeting_count
# Sonny.greet(Jordan)
# Sonny.greeting_count
# Sonny.greet(Jordan)
# Sonny.greeting_count
# Sonny.greet(Jordan)
# Sonny.greeting_count
# Sonny.greet(jordan)
# Sonny.greeting_count

# print(Sonny.__str__())

# Exercise 2. Make your own class

# class Vehicle:
#     def __init__ (self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def print_info(self):
#         print ('Vehicle information: {} {} {}'.format(self.year, self.model, self.make))
#             # f' Vehicle information: {self.year} {self.model} {self.make}')


# car = Vehicle ('Nissan', 'Leaf', '2015')
# car.print_info()

