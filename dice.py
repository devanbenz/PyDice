import random as rng

dice_on = True
rolls = []

def six():
    roll6 = rng.randint(1,6)
    print("You roll a six sided dice and... you get a {0}".format(roll6))
    rolls.append(roll6)
def three():
    roll3 = rng.randint(1,3)
    print("You roll a six sided dice and... you get a {0}".format(roll3))
    rolls.append(roll3)

def main():
    print("Welcome to dice.py")
    while dice_on:
        userInput = input("Please select - \n[1] for a six sided dice roll!\n[2] for a three sided dice roll!: ")
        if userInput == '1':
            six()
            print("Dice rolls: {0}".format(rolls))
            while True:
                userInput = input("Roll again? Y/N: ")
                userInput.upper()
                if userInput == "Y":
                    break
                elif userInput == "N":
                    print("Thank you, goodbye!")
                    exit()
                else:
                    print("Bad input")
        elif userInput == '2':
            three()
            print("Dice rolls: {0}".format(rolls))
            while True:
                userInput = input("Roll again? Y/N: ")
                userInput.upper()
                if userInput == "Y":
                    break
                elif userInput == "N":
                    print("Thank you, goodbye!")
                    exit()
                else:
                    print("Bad input")
        else:
            print("Bad input")

main()