import rolls as roll

dice_on = True

def main():
    print("Welcome to dice.py")
    while dice_on:
        userInput = input("Please select - \n[1] for a twenty sided dice roll!\n[2] for a twelve sided dice roll!: ")
        if userInput == '1':
            roll.twenty()
            print("Dice rolls: {0}".format(roll.prev_rolls))
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
            roll.twelve()
            print("Dice rolls: {0}".format(roll.prev_rolls))
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