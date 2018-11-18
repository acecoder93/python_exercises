# 1. Uppercase a String
# string = "My name is Anuj"
# print( str.upper(string))

# 2. Capitalize a String
# string = "it is time to capitalize this sentence."
# new = string.capitalize()
# print (new)

# 3. Reverse a string
# question = str(input('Please enter a string: ')) 
# reverse = question[::-1]
# print (reverse)

# 4. Leetspeak

# question = str.upper(input('Please enter a paragraph of text: '))
# answer = ""

# for n in question:
#     new = n
#     if new == "A":
#         new = "4"
#     elif new == "E":
#         new = "3"
#     elif new == "G":
#         new = "6"
#     elif new == "I":
#         new = "1"
#     elif new == "O":
#         new = "0"
#     elif new == "S":
#         new = "5"
#     elif new == "T":
#         new = "7"
#     answer = answer + new
# print (answer)

# 5. Long-long Vowels

# given = str.lower(input('Please provide a string: '))
# long_vowels = [ 'aa', 'ee', 'ii', 'oo', 'uu']
# result = ''

# for i in range(len(given)):
#     twoletters = given[i:i+2]
#     if twoletters in long_vowels:
#         result += given[i] * 4
#     else:
#         result += given[i]

# print(result)

# 6. Caesar Cipher - Review with Katy
# given = str.lower('lbh zhfg hayrnea jung lbh unir yrnearq')

# for n in given:
    