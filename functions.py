import random as r

#defines a function called guessTheNumber
#the brackets beside the name indicate that this function is given a piece of information
#the name of that information needs to be consistent inside of the function BUT
#it does NOT have to be the same name as the variable given to it ***VERY IMPORTANT***
def guessTheNumber(answer):
    userNumber = int(input("Please guess a number: "))
    if userNumber == answer:
        print("Correct! You win!")
        return True
    elif userNumber > answer:
        print("Nope! Too high!")
        return False
    elif userNumber < answer:
        print("Nope! Too low!")
        return False
    else:
        print("You dun did a stupid!")
        return False