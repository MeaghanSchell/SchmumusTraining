import random
# age = 20
# age2 = 30
# price = 19.95
# first_name = 'Meaghan'
# is_online = False
# is_online2 = True
# first_name2 = 'John Smith'
# is_newpatient = True
# print(first_name2)
# print(age)
# print(is_newpatient)
#
# print(first_name2, age, is_online2)
# print("Hello, I am John Smith. I am 20 years and a new patient.")
# print("Hello, my name is " + str(first_name2) + " and I am " + str(age) + " years old!")

# name = input("What is your name? ")
# print("Hello" + name)
# birth_year = input("Enter your birth year: ")
# int(birth_year)
# age = 2023 - int(birth_year)
# print(age)

#Built in Functions
# int() - For whole numbers
# float() - For decimals
# bool() - True and False
# str() - Anything you can't do math on

#Calulator Code
# first_coefficient = input("First: ")
# second_coefficient = input("Second: ")
# sum = (float(first_coefficient) + float(second_coefficient))
# print("Sum: ",sum)

#Calculator Code more efficient
# first = float(input("Frist"))
# second = float(input("Second"))
# sum = first + second
# print("Sum: ", sum)

# course = 'Python for Beginners'
# print(course.upper())
# print(course)
# print(course.lower())
# print(course.replace('for','4'))

# > is greater than
# >= is great than or equal too
# < is less than
# <= is less than or equal too
# == is equal to
# != is not equal to

# If statements
# temperature = 25
# if temperature > 30:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif temperature > 20:
#     print("It's a nice day")
# elif temperature >10:
#     print("It's abit cold")
# else:
#     print("It's cold")
# print("Done")

# If Statement
# weight = float(input("Weight: "))
# unit = input("K or L")
# if unit == "K":
#     print("Weight in Lbs", weight/0.453)
# if unit == "L":
#     print("Weight in Kg", weight*0.453)

#Doug's first challenge for me!
# metal = input("Metal")
# unit = input("Kg or Lbs")
# weight = float(input("How many Kg or Lbs"))
#
# if unit.lower() == "k" or unit.lower() == "kg":
#     weight = weight
# if unit.lower() =="l" or unit.lower() == "lbs":
#     weight = weight*0.453
# if metal == "gold" or metal == "au":
#     print("Price $", weight*1653.90)
# if metal == "silver" or metal == "ag":
#     print("Price $", weight*912.76)




#PUZZLE ONE
#create a number-guessing game
#have the computer generate a random number, then ask the user to guess
#give the user three attempts to get the correct number
#if the user gets it wrong, tell them whether they're too high or too low
#if the user gets it right, don't ask them again
# myFirstRandomNumber = random.randint(0, 10)

# Meaghan's Number Guessing Game
theRandomNumber = random.randint(0, 10)
userHasWon = False
print("We are choosing a number. Get ready to guess!")
Attempt1 = float(input("Attempt 1 - Guess a random number."))
if Attempt1 == theRandomNumber:
    print("Yay! You guessed the correct number!")
    print("The random number was" + str(theRandomNumber))
    userHasWon = True
if Attempt1 != theRandomNumber:
    print("You have guessed incorrectly. You have two tries left.")
if userHasWon == False:
    Attempt2 = float(input("Attempt 2 - Guess another random number."))
    if Attempt2 == theRandomNumber:
        print("Yay! You guessed the correct number!")
        print("The random number was" + str(theRandomNumber))
        userHasWon = True
    if Attempt2 != theRandomNumber:
        print("You have guessed incorrectly. You have one try left. May the odds be ever in your favour.")
if userHasWon == False:
    Attempt3 = float(input("Attempt 3 - This is your last attempt to guess random number."))
    if Attempt3 == theRandomNumber:
        print("Yay! You did it! You guessed the correct number!")
        print("The random number was" + str(theRandomNumber))
    if Attempt3 != theRandomNumber:
        print("Wah, wah, wah... You have guessed incorrectly. Please play again.")









