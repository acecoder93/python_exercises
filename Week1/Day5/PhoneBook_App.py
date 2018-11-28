# Phone Book App

print ('Welcome to the latest version of hthe Electronic Phone Book')
print ('Please see the list below of all of the options that are available.')

print ('''Electronic Phone Book
        ---------------------
        1. Look up an Entry
        2. Set an entry
        3. Delete an entry
        4. List all entries
        5. Quit ''')
options = int(input('Please select an option: (1-5)? '))
myDictionary = [{
    "John Doe" : "111-111-1111",
    "Mamma Mia" : "222-222-2222",
    "Mickey Mouse" : "333-333-3333",
    "Ric Flair" : "444-444-4444"}
    ,{
    "first_name" : "John",
    "last_name" : "Doe",
    "phone_number" : "888-888-8888"

}]


def look_up():
    look_up = str.lower(input('Please provide the person\'s name: '))
    if look_up == myDictionary[name]:
        print ('{}\'s phone number is: {}'.format(name,myDictionary[name]))
def set_entry():
    set_name = str.lower(input('Please provide the person\'s name: '))
    set_number = int((input('Please provide the person\'s phonenumber: ')))

def delete_entry():
    delete_entry = str.lower(input('Please provide the person\'s name: '))

def list_all_entries():
    list_all_entries = str.lower(input('Would you like to list all entries? (Y or N) '))

while options != range(1,5,1):
    if options == 1:
        look_up()
    elif options == 2:
        set_entry()
    elif options == 3:
        delete_entry()
    elif options == 4:
        list_all_entries()
    elif options == 5:
        finish = str.lower(input('Quit the application? (Y or N) '))
    else:
        options = int(input('What do you want to do (1-5)? '))
#   break

# if myDictionary[look_up] in myDictionary:
#     print (myDictionary.value())



# look_up = str.lower(input('Please provide the person\'s name: '))
# set_entry = str.lower(input('Please provide the person\'s name and phone number: '))
# delete_entry = str.lower(input('Please provide the person\'ns name: '))
# list_all_entries = str.lower(input('Would you like to list all entries? (Y or N) '))

