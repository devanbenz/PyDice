import random as rng
prev_rolls = []

# D20
def twenty():
    roll20 = rng.randint(1,20)
    print("You roll a twenty sided dice and... you get a {0}".format(roll20))
    prev_rolls.append(roll20)

# D12
def twelve():
    roll12 = rng.randint(1,12)
    print("You roll a twelve sided dice and... you get a {0}".format(roll12))
    prev_rolls.append(roll12)

# D10
def ten():
    roll10 = rng.randint(1,10)
    print("You roll a ten sided dice and... you get a {0}".format(roll10))
    prev_rolls.append(roll10)

# D8
def eight():
    roll8 = rng.randint(1,8)
    print("You roll an eight sided dice and... you get a {0}".format(roll8))
    prev_rolls.append(roll8)

# D6
def six():
    roll6 = rng.randint(1,6)
    print("You roll a six sided dice and... you get a {0}".format(roll6))
    prev_rolls.append(roll6)

# D4
def four():
    roll4 = rng.randint(1,4)
    print("You roll a four sided dice and... you get a {0}".format(roll4))
    prev_rolls.append(roll4)

