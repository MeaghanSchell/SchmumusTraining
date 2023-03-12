#imports are ways to include libraries of prewritten code
#imports always go at the top 
#in this case, I'm adding the 'random' library
#I can then reference the libary by using its name
import random

#randint() is a method that generations a random integer
#the two numbers are a range; it will generate between 0 and 10
#it will not include 0, but will include 10
myFirstRandomNumber = random.randint(0, 10)


#PUZZLE ONE
#create a number-guessing game
#have the computer generate a random number, then ask the user to guess
#give the user three attempts to get the correct number
#if the user gets it wrong, tell them whether they're too high or too low
#if the user gets it right, don't ask them again

#PUZZLE TWO
#create a grade average calculator
#get a name and three scores from the user
#average the three scores and match it to a letter grade
#assume the letter grades are: 0-49%: F, 50-59% D, 60-74% C, 75-84% B, 85-100% A
#output should look like: Schmumu - A - 100
