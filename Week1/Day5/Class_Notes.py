# Dictionary Lecture Notes
# Dictionary - store value to a key


# Example 1 - Creating a Dictionary
myContactList = {
    "first_name" : "Anuj", # Key can be different type of datatypes (Boolean, String, Integer)
    "last_name" : "Saheba",
    "age" : 25, 
    12 : "street",
    "friends" : {
        "first_name" : "Erick",
        "last_name" : "Thai",
        "occupation" : "student"
    }
}

# first_name = myContactList["first_name"]  # Information within a dictionary is indexed by the key ex: myContactList["first_name"]  will output Anuj
# first_name = myContactList.get("dog") # Get() - a safe way to look for something within a dictionary without providing user a large python error message
# print (first_name)

# isItThere = "dog" in myContactList # In allows for "True" or "False"
# print (isItThere)

# if ("last_name" in myContactList):
#     print(myContactList["last_name"])

# Setting Values
# myList = ["one", "two", "three"]

# myList[0] = 1
# print (myList)
# print (myContactList["age"]) #shows value of age
# myContactList["age"] = 50 #setting age to new value of "50"
# print (myContactList["age"]) #prints out new value

# Keys () & Values ()
# only_keys = myContactList.keys()
# print (only_keys)

# only_values = myContactList.values()
# print (only_values)


# Deleting items from a dictionary del ()
# del myContactList[12]
# print (myContactList.keys())


# Iterating
# for key, value in myContactList.items():
#     print(("{key} {value}").format(key = key, value = value))

# Nesting - in my example, "Friends" is nested within myContactsList - NEED TO OBTAIN UPDATED EXAMPLE FROM Veronica's GitHub

contact = [
    {"first_name": "",
    "last_name": "",
    "email": "",
    "phone": {
        "home": "",
        "cell": ""
    }
    }

    {"first_name": "",
    "last_name": "",
    "email": "",
    "phone": {
        "home": "",
        "cell": ""
    }},
    {},
]
