#imports are ways to include libraries of prewritten code
#imports always go at the top 
#in this case, I'm adding the 'random' library
#I can then reference the libary by using its name
import random
import functions
import numpy

#randint() is a method that generations a random integer
#the two numbers are a range; it will generate between 0 and 10
#it will not include 0, but will include 10
# myFirstRandomNumber = random.randint(0, 10)


#PUZZLE ONE
#create a number-guessing game
#have the computer generate a random number, then ask the user to guess
#give the user three attempts to get the correct number
#if the user gets it wrong, tell them whether they're too high or too low
#if the user gets it right, don't ask them again

# userHasWon = False
# functions.guessTheNumber()
# functions.guessTheNumber()
# functions.guessTheNumber()

# if userHasWon == False:
    #here we are CALLING the function that is defined in the functions file
#     userHasWon = functions.guessTheNumber(myFirstRandomNumber)
# if userHasWon == False:
#     userHasWon = functions.guessTheNumber(myFirstRandomNumber)
# if userHasWon == False:
#     userHasWon = functions.guessTheNumber(myFirstRandomNumber)



    

#PUZZLE TWO
#create a grade average calculator
#get a name and three scores from the user
#average the three scores and match it to a letter grade
#assume the letter grades are: 0-49%: F, 50-59% D, 60-74% C, 75-84% B, 85-100% A
#output should look like: Schmumu - A - 100

#def means we're starting a function definition
def getAGrade():
    while True:
        grade = input("Please enter a grade: ")
        if not grade.isnumeric():
            print("That's not a number!")
        else:
            return int(grade)

userName = ''
# firstGrade = 0 
# secondGrade = 0
# thirdGrade = 0

#array is a list of values (any kind of value)
#arrays have functions append, pop, etc.
gradeArray = []

#input() is a function that returns the value entered
userName = input("Please enter your name: ")
while len(gradeArray) < 3:
    gradeArray.append(getAGrade())

#calculation
# gradeAverage = (firstGrade + secondGrade + thirdGrade) / 3
gradeAverage = numpy.mean(gradeArray)
letterGrade = ''

#find letter grade
if gradeAverage >= 0 and gradeAverage <= 49:
    letterGrade = 'F'
elif gradeAverage >= 50 and gradeAverage <= 59:
    letterGrade = 'D'
elif gradeAverage >= 60 and gradeAverage <= 74:
    letterGrade = 'C'
elif gradeAverage >= 75 and gradeAverage <= 84:
    letterGrade = 'B'
elif gradeAverage >= 85 and gradeAverage <= 100:
    letterGrade = 'A'

print(f'Name: {userName} - Grade Average: {round(gradeAverage, 2)} - Letter Grade: {letterGrade}')




#NO MORE SCROLLING!







#ONLY CHEATERS SCROLL FURTHER!!




# userName = input("Please enter a name: ")
# userGrade1 = float(input("Enter first grade: "))
# userGrade2 = float(input("Enter second grade: "))
# userGrade3 = float(input("Please enter third grade: "))
# userGradeAverage = (userGrade1 + userGrade2 + userGrade3) / 3
# userLetterGrade = ""
# if userGradeAverage < 50:
#     userLetterGrade = "F"
# elif userGradeAverage >= 50 and userGradeAverage < 60:
#     userLetterGrade = "D"
# elif userGradeAverage >= 60 and userGradeAverage <= 74:
#     userLetterGrade = "C"
# elif userGradeAverage >= 75 and userGradeAverage <= 84:
#     userLetterGrade = "B"
# elif userGradeAverage >= 85:
#     userLetterGrade = "A"
# print(f"{userName} - {userLetterGrade} - {userGradeAverage}")
#f-strings put an f before the string, and then wrap variables inside curly braces