import random as rng

characterInfo = {}
characterCreationOn = True

def charName():
    while characterCreationOn:
        userInput = input("Please type in a name for your character: ")
        if len(userInput) > 50:
            print("Please use a shorter name.")
        else:
            print("Welcome to Dice.py {0}".format(userInput))
            return userInput

def charClass():
    while characterCreationOn:
        print("Please choose a class from the following list\n [1]Barbarian")
        userInput = input("Choice: ")
        if userInput == '1':
            print("You're a barbarian!")
            userInput = "barbarian"
            return userInput
        else:
            print("Incorrect Selection, please try again.")

#testing
cName = charName()
cClass = charClass()
characterInfo['name'] = cName
characterInfo['class'] = cClass
print(characterInfo)



