# Step 1. Guess a Number
# secretNumber = int(5)
# guess = int(input('I am thinking of a number between 1 and 10. What\'s the secret number? '))
# while guess != secretNumber:
#     guess = int(input('Please try again. What\'s the secret number? '))
# if guess == secretNumber:
#     print ("You got it!")

# Step 2. Give High-Low Hint
# secretNumber = int(5)
# guess = int(input('I am thinking of a number between 1 and 10. What\'s the secret number? '))
# while guess != secretNumber:
#     if guess < secretNumber:
#         guess = int(input('Please try again. Your guess is too low. What\'s the secret number? '))
#     elif guess > secretNumber:
#         guess = int(input('Please try again. Your guess is too high. What\'s the secret number? '))
# if guess == secretNumber:
#     print ("You got it!")

# Step 3. Randomly Generated Secret Number
# import random

# secretNumber = int(random.randint(1,10))
# guess = int(input('I am thinking of a number between 1 and 10. What\'s the secret number? '))
# while guess != secretNumber:
#     if guess < secretNumber:
#         guess = int(input('Please try again. Your guess is too low. What\'s the secret number? '))
#     elif guess > secretNumber:
#         guess = int(input('Please try again. Your guess is too high. What\'s the secret number? '))
# if guess == secretNumber:
#     print ("You got it!")

#Step 4. Limit Number of Guesses
# import random

# secretNumber = int(random.randint(1,10))
# guess = int(input('I am thinking of a number between 1 and 10. What\'s the secret number? '))

# count = 0
# while count < 5:
#     count += 1
#     if guess < secretNumber:
#         guess = int(input('Please try again. Your guess is too low. What\'s the secret number? '))
#     elif guess > secretNumber:
#          guess = int(input('Please try again. Your guess is too high. What\'s the secret number? '))

# if guess == secretNumber:
#     print ("You got it!")

# if guess != secretNumber:
#     print ("Sorry, maybe next time!")

# Bonus: Play Again
# import random

# secretNumber = int(random.randint(1,10))
# guess = int(input('I am thinking of a number between 1 and 10. What\'s the secret number? '))

# def game(guess):
#     count = 0
#     while count < 5:
#         count += 1
#         if guess < secretNumber:
#             guess = int(input('Please try again. Your guess is too low. What\'s the secret number? '))
#         elif guess > secretNumber:
#             guess = int(input('Please try again. Your guess is too high. What\'s the secret number? '))
#     if guess == secretNumber:
#         print ("You got it!")
#     if guess != secretNumber:
#         print ("Sorry, maybe next time!")
# game(guess)

# playagain = str.upper((input('Would you like to play again? (Y or N) ')))
# if playagain == "Y":
#     game(guess)
# elif playagain == "N":
#     print ("Sounds good! Have a nice day!")
# else:
#     print ("Invalid Input")

