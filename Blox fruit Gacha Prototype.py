# blox fruit Gacha prototy

import random

def main():

    common = ["Rocket", "Spin", "Blade", "Spring", "Bomb", "Smoke", "Spike"]
    uncommon = ["Flame", "Ice", "Sand", "Dark", "Eagle", "Diamond"]
    rare = ["Light", "Rubber", "Ghost", "Magma"]
    legendary = ["Quake", "Buddha", "Love", "Creation", "Spider", "Sound", "Phoenix", "Portal", "Lightning", "Pain", "Blizzard"]
    mythical = ["Gravity", "Mammoth", "T-Rex", "Dough", "Shadow", "Venom", "Gas", "Spirit", "Tiger", "Yeti", "Magnet", "Kitsune", "Control", "Dragon"]

    categories = [common,uncommon,rare,legendary,]

    spin = random.randint(1,100)

    if spin >= 45:

        print("its common fruit")

        commonchance(common)

    elif spin >= 25:

        print("its an uncommon fruit")

        uncommonchance(uncommon)

    elif spin >= 10:

        print("its rare fruit")

        rarechance(rare)

    elif spin >= 5:

        print("its an legerdary fruit")

        legendarychance(legendary)

    elif spin >= 1:

        print("its an mythic")

        mythicalchance(mythical)

def looping():

    ask = str(input("Do you want to use progream again?(yes/no):"))

    while ask.lower() == "yes":

        main()

        ask = str(input("Do you want to use progream again?(yes/no):"))

    print("progream has been ended")

def commonchance(common):

    spin1 = random.randint(1,100)

    if spin1 >= 81:

            print("You got:",common[0])

    elif spin1 >= 63:
    
            print("You got:",common[1])

    elif spin1 >= 47:
        
            print("You got:",common[2])

    elif spin1 >= 33:
        
            print("You got:",common[3])

    elif spin1 >= 21:
        
            print("You got:",common[4])

    elif spin1 >= 10:
        
            print("You got:",common[5])

    elif spin1 >= 1:
        
            print("You got:",common[6])

def uncommonchance(uncommon):

    spin2 = random.randint(1,100)

    if spin2 >= 76:

            print("You got:",uncommon[0])

    elif spin2 >= 56:
    
            print("You got:",uncommon[1])

    elif spin2 >= 39:
        
            print("You got:",uncommon[2])

    elif spin2 >= 24:
        
            print("You got:",uncommon[3])

    elif spin2 >= 11:
        
            print("You got:",uncommon[4])

    elif spin2 >= 1:
        
            print("You got:",uncommon[5])

def rarechance(rare):

    spin3 = random.randint(1,100)

    if spin3 >= 66:

            print("You got:",rare[0])

    elif spin3 >= 41:
    
            print("You got:",rare[1])

    elif spin3 >= 19:
        
            print("You got:",rare[2])

    elif spin3 >= 1:
        
            print("You got:",rare[3])

def legendarychance(legendary):

    spin4 = random.randint(1,100)

    if spin4 >= 87:

            print("You got:",legendary[0])

    elif spin4 >= 74:
    
            print("You got:",legendary[1])

    elif spin4 >= 62:
        
            print("You got:",legendary[2])

    elif spin4 >= 51:
        
            print("You got:",legendary[3])

    elif spin4 >= 41:
        
            print("You got:",legendary[4])

    elif spin4 >= 32:
        
            print("You got:",legendary[5])

    elif spin4 >= 24:
        
            print("You got:",legendary[6])

    elif spin4 >= 17:
        
            print("You got:",legendary[7])

    elif spin4 >= 11:
        
            print("You got:",legendary[8])

    elif spin4 >= 6:
        
            print("You got:",legendary[9])

    elif spin4 >= 1:
        
            print("You got:",legendary[10])

def mythicalchance(mythical):

    spin5 = random.randint(1,100)

    if spin5 >= 89:

            print("You got:",mythical[0])

    elif spin5 >= 78:
    
            print("You got:",mythical[1])

    elif spin5 >= 68:
        
            print("You got:",mythical[2])

    elif spin5 >= 59:
        
            print("You got:",mythical[3])

    elif spin5 >= 50:
        
            print("You got:",mythical[4])

    elif spin5 >= 42:
        
            print("You got:",mythical[5])

    elif spin5 >= 34:
        
            print("You got:",mythical[6])

    elif spin5 >= 27:
        
            print("You got:",mythical[7])

    elif spin5 >= 21:
        
            print("You got:",mythical[8])

    elif spin5 >= 16:
        
            print("You got:",mythical[9])

    elif spin5 >= 11:
        
            print("You got:",mythical[10])

    elif spin5 >= 7:
        
            print("You got:",mythical[11])

    elif spin5 >= 4:
        
            print("You got:",mythical[12])

    elif spin5 >= 1:
            
            print("You got:",mythical[13])

            dragontypes = ["East Dragon","West Dragon"]

            choosen = random.choice(dragontypes)

            print("And you got:",choosen)

main()

# looping()