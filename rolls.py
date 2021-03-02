import random as rng
prev_rolls = []

#Six sided Dice
def six():
    roll6 = rng.randint(1,6)
    print("You roll a six sided dice and... you get a {0}".format(roll6))
    prev_rolls.append(roll6)

#Three sided Dice
def three():
    roll3 = rng.randint(1,3)
    print("You roll a six sided dice and... you get a {0}".format(roll3))
    prev_rolls.append(roll3)