# myList

# myShoppingList = ['apples', 'kale', 'ginger', 'spinach']
# howmany = len(myShoppingList)

# myShoppingList[0] #output apples
# myShoppingList[1] #output kale
# myShoppingList[2] #output ginger
# myShoppingList[3] #output spinach

# partial_list = myShoppingList[3:5]
# partial_length = len(partial_list)

# print (myShoppingList)
# print (howmany)
# print (partial_list)
# print (partial_length)

# myShoppingList.insert (3, "COOKIES")
# myShoppingList.extend ([3, 4, 5, "PHONG"])
# myShoppingList.pop ()
# index = myShoppingList.index ('COOKIES')

# print (myShoppingList)
# print (index)

# newlist = [23, 1232, 231, 452, 21]
# print (newlist.sort())

# newgroceries = myShoppingList.copy()
# print (newgroceries)
# myShoppingList.append("oranges")
# howmany = len(myShoppingList)

# print (myShoppingList)
# print (howmany)

# myName = "Anuj"
# print (myName[0])
# print (len(myName))

# sentence = "My name is Anuj"
# print (sentence.index(' '))

# set1 = [123 , 131, 34, 3]
# set2 = [-1, -2, -3]
# print (set1 + set2)

# myTuples = (1, "Sandhya", "Ram")
# myTuples[0] = "hello"

# r = range 10)
# print (r)

# # # for loop nested, example is a multiplication table
# for outerindex in range (1,11, 2):
#     # print ("Index:", index)
#     for innerindex in range (1, 11, 3):
#         print ((outerindex), " x ", innerindex, " = ", (outerindex * innerindex))


# president = ['George', 'W', 'Bush']
# print (president)

# for name in president:
#     # print (president.index(name)) #name represents a value inside the list
#     print (president.pop())

# print ("my list length", len(president) )

# for name in president:
#     print

#Exercise below is used to multiple and sum up the items from list 1 and list 2 and add it into list 3.
list1 = [1, 5, 3, 6, 7]
list2 = [3, 6, 9, 10, 2]
list3 = []

for num_1 in list1:
    total = 0
    for num_2 in list2:
        total += num_1 * num_2
    list3.append(total)
print(list3)
