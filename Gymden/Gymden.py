import random

import time
import os
import sys


def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)


def typingInput(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    value = input()
    return value


inventory = ["wrench", "screwdriver"]

equipped = "wrench"

health = 100

skill_pilot = random.randint(7, 8)
skill_mechanic = random.randint(1, 20)
skill_warfare = random.randint(1, 20)

# Invetory Functions


def addtoinventory(item):
    inventory.append(item)
    typingPrint("You found a " + str(item) + "!")


def printinventory():
    typingPrint("You have the following items in you inventory:\n")
    for i in inventory:
        typingPrint(i)
        typingPrint("\n")
    typingPrint("\n")

###

# Items that can be found


common_item1 = "combat knife"

common_item2 = "9mm revolver"

epic_item1 = "pulse rifle"

epic_item2 = "Plasma Thrower"

Mythical_item = "comically large spoon"

###

###                   ////// Events for planet one   ///////                    ###


def Planet1_event1(health):
    plan = typingInput(
        "You decent towards the planet a bit to quickly, the friction from the atmosphere makes your ship hotter and hotter. \n What is your plan of action? \n[1] Eavasiv Manuvers \n[2] Override the engine \n[3] Shoot the control panel")
    if plan == "1":
        difficulty = random.randint(1, 20) + int(skill_pilot)
        if difficulty >= 100:
            typingPrint(
                "You succsesfully managed to control the ship making it to orbit")
            return health
        elif difficulty >= 10:
            typingPrint(
                "You managed to control the ship with your skills and get back to orbit, but you didnt come out of it unscaved \n You lost: 10 health")
            health -= 10
            return int(health)
        else:
            typingPrint(
                "You failed to control the ship and burned up in the atmosphere\n\n GAME OVER")
            health -= 100
            return int(health)
    elif plan == "2":
        difficulty = random.randint(1, 20) + int(skill_mechanic)
        if difficulty >= 15:
            typingPrint(
                "You managed to perfectly override the engine giving your ship enough raw power to return to orbit")
            return health
        elif difficulty >= 10:
            typingPrint(
                "You managed to override the engine but the ride back to orbit was not the smoothest \n you lost 10 health")
            health -= 10
            return int(health)
        else:
            typingPrint(
                "You failed to ovveride the engine causeing your ship to explode in a firery explosion\n\n GAME OVER")
            health -= 100
            return int(health)
    elif plan == "3":
        difficulty = random.randint(1, 20) + int(skill_warfare)
        if difficulty >= 15:
            typingPrint(
                "You shoot the control panel right in the center causing safe mode to activate and saving your sorrow ass. ")
            return health
        elif difficulty >= 10:
            typingPrint(
                "You decide that the smartest move is to shoot the control panel, the ships controls are now gone and you are gonna die\n\n GAME OVER")
            health -= 100
            return int(health)
        else:
            typingPrint(
                "You shoot the control panel which activates the ships intruder defense system, initianting self destruct. You explode.\n\n GAME OVER")
            health -= 100
            return int(health)


def Planet1_event2():
    typingPrint("\n\nYou slowly decend towards the planet without any major problems. \nYou decide to land next to a small remote outpost on the planet to not attract any unwanted attention.\nThis outpost has been abandoned for a long time but you still managed to find a few supplies scatterd around \n")
    luck = random.randint(1, 3)
    if luck == 1:
        common = random.randint(1, 2)
        if common == 1:
            common = "combat knife"
            if common in inventory:
                typingPrint(
                    "You found a combat knife but since you already have one you threw it away")
            else:
                inventory.append(common)
                typingPrint("You found a combat knife!")
        else:
            common = "9mm revolver"
            if common in inventory:
                typingPrint(
                    "You found a 9mm revolver but since you already have one you threw it away")
            else:
                inventory.append(common)
                typingPrint("You found a 9mm revolver!")
    elif luck == 2:
        rare = random.randint(1, 2)
        if rare == 1:
            rare = "pulse rifle"
            if rare in inventory:
                typingPrint(
                    "You found a pulse rifle but since you already have one you threw it away")
            else:
                inventory.append(rare)
                typingPrint("You found a pulse rifle!")
        else:
            rare = "plasma thrower"
            if rare in inventory:
                typingPrint(
                    "You found a plasma thrower but since you already have one you threw it away")
            else:
                inventory.append(rare)
                typingPrint("You found a plasma thrower!")
    else:
        spoon = "comically large spoon"
        if spoon in inventory:
            typingPrint(
                "You found a comically large spoon but since you already have one you threw it away")
        else:
            inventory.append(spoon)
            typingPrint("You found a comically large spoon!")


def Planet1_event3(health, skill_warfare):
    xeno_level = random.randint(1, 15)
    typingPrint("\n\nYou land at the planet without any problems. \nYou only managed to take a few steps from the ship before you are faced with a vile level " + str(xeno_level) + " xeno")
    xeno_health = random.randint(1, 15) + int(xeno_level)
    if equipped == "wrench" and "screwdriver":
        bonus_attack = 0
    elif equipped == "9mm revolver" and "combat knife":
        bonus_attack = 3
    elif equipped == "Plasma Thrower" and "pulse rifle":
        bonus_attack = 6
    elif equipped == "comically large spoon":
        bonus_attack = 10
    elif equipped == "small stim" and "stim" and "large stim":
        bonus_attack = -15
    your_attack = int(skill_warfare) + int(bonus_attack)

    while xeno_health > 0 and health > 0:
        typingPrint("\nYou attack the xeno with your " + equipped +
                    " dealing " + str(your_attack) + " damage!\n")
        xeno_health = int(xeno_health) - int(your_attack)
        xeno_attack = int(xeno_level) + random.randint(1, 10)
        typingPrint("The xeno strikes back dealing " +
                    str(xeno_attack) + " damage!\n")
        health = int(health) - int(xeno_attack)
        typingPrint("Your enemy have " + str(xeno_health) +
                    " health!\nYou have " + str(health) + " health!\n")
        if xeno_health <= 0:
            typingPrint("YOU WON\nYou gained 1 level in warfare")
        elif health <= 0:
            typingPrint("YOU LOST")

    return health, skill_warfare


def Planet1_event4():
    health_item_size = random.randint(1, 3)
    if health_item_size == 1:
        health_item = "small stim"

    elif health_item_size == 2:
        health_item = "stim"
    else:
        health_item = "large stim"
    typingPrint("\n\nYou enter the planets atmosphere and land next to an old hospital\nYou scavenge the building for supplies\nYou found " + health_item)
    inventory.append(health_item)


def Planet1_event5():
    typingPrint("\n\nYou fly down to the planets atmosphere, you notice that the winds down here appear to be quite extreme.\nAfter a short while inside the planets atmosphere you get hit by some debri. \nCausing a violent collision throwing you into a wall.\nYou decide it is best to leave this planet be and return to orbit. \n\nYou lost 15 health")


def Planet1_event6(health, skill_warfare):
    action = typingInput(
        "\n\nYou have succsessfully landed on the planet and now start to explore,\nyou find a great number of new plants among them an enormous one.\nWhat is your action? \n [1] approach \n [2] continue exploring \n [3] Go back to the ship ")
    plant_damage = random.randint(1, 20)
    if action == ("1"):
        typingPrint(
            "\n\n This plant is an carnivor and you have fallen right in it's trap.")
        health -= plant_damage
        if health <= 0:
            typingPrint(
                "\nThe plant grabbed you and smacked you to the ground leading to your inevitable demise")
            return health, skill_warfare
        elif health > 0:
            typingPrint(
                "You managed to escape with your life \nYou have " + str(health) + " health left")
            return health, skill_warfare
    elif action == ("2"):
        typingPrint(
            "You continue exploring and find a crashed ship,\n you look inside and find a chest, \nyou open the chest...")
        luck = random.randint(1, 3)
        if luck == 1:
            common = random.randint(1, 2)
            if common == 1:
                common = "combat knife"
                if common in inventory:
                    typingPrint(
                        "You found a combat knife but since you already have one you threw it away")
                    return health, skill_warfare
                else:
                    inventory.append(common)
                    typingPrint("You found a combat knife!")
                return health, skill_warfare
            else:
                common = "9mm revolver"
                if common in inventory:
                    typingPrint(
                        "You found a 9mm revolver but since you already have one you threw it away")
                    return health, skill_warfare
                else:
                    inventory.append(common)
                    typingPrint("You found a 9mm revolver!")
                return health, skill_warfare
        elif luck == 2:
            rare = random.randint(1, 2)
            if rare == 1:
                rare = "pulse rifle"
                if rare in inventory:
                    typingPrint(
                        "You found a pulse rifle but since you already have one you threw it away")
                    return health, skill_warfare
                else:
                    inventory.append(rare)
                    typingPrint("You found a pulse rifle!")
                return health, skill_warfare
            else:
                rare = "plasma thrower"
                if rare in inventory:
                    typingPrint(
                        "You found a plasma thrower but since you already have one you threw it away")
                    return health, skill_warfare
                else:
                    inventory.append(rare)
                    typingPrint("You found a plasma thrower!")
                return health, skill_warfare
        else:
            spoon = "comically large spoon"
            if spoon in inventory:
                typingPrint(
                    "You found a comically large spoon but since you already have one you threw it away")
                return health, skill_warfare
            else:
                inventory.append(spoon)
                typingPrint("You found a comically large spoon!")
            return health, skill_warfare

    elif action == ("3"):
        xeno_level = random.randint(1, 15)
        typingPrint(
            "You go back to the ship and see a xeno trying to steal your ship,\n you have to fight it to get your ship back.")
        xeno_health = random.randint(1, 15) + int(xeno_level)
        if equipped == "wrench" and "screwdriver":
            bonus_attack = 0
        elif equipped == "9mm revolver" and "combat knife":
            bonus_attack = 3
        elif equipped == "Plasma Thrower" and "pulse rifle":
            bonus_attack = 6
        elif equipped == "comically large spoon":
            bonus_attack = 10
        elif equipped == "small stim" and "stim" and "large stim":
            bonus_attack = -15
        your_attack = int(skill_warfare) + int(bonus_attack)

        while xeno_health > 0 and health > 0:
            typingPrint("\nYou attack the xeno with your " + equipped +
                        " dealing " + str(your_attack) + " damage!\n")
            xeno_health = int(xeno_health) - int(your_attack)
            xeno_attack = int(xeno_level) + random.randint(1, 10)
            typingPrint("The xeno strikes back dealing " +
                        str(xeno_attack) + " damage!\n")
            health = int(health) - int(xeno_attack)
            typingPrint("Your enemy have " + str(xeno_health) +
                        " health!\nYou have " + str(health) + " health!\n")
            if xeno_health <= 0:
                typingPrint("YOU WON\nYou gained 1 level in warfare")
                skill_warfare += 1

            elif health <= 0:
                typingPrint("YOU LOST")

        return health, skill_warfare
    else:
        typingPrint("TRY AGAIN!")
#################################################################################################

# //// GAME CODE //// #


Start = typingInput("Do you want to play the game y/n? --> ")

if Start == "y" and "yes":
    typingPrint("good")
else:
    typingPrint("Yes you do ")


player_name = input("\n Enter your name here --> ")

W = typingInput("Welcome " + player_name +
                ",\nWe will now randomize your capabilities, press ENTER to continue. -->")


typingPrint("Your skills are:\n Piloting: " + str(skill_pilot) + "\n mechanical: " +
            str(skill_mechanic) + "\n Warfare: " + str(skill_warfare) + " ")

while int(health) > 0:
    if int(health) <= 0:
        typingPrint("\n\n GAME OVER")
        break
    else:
        Planet_1 = "New planet"

        planet_choice = typingInput("\n\n What do you want to do ?" "\n [1] " +
                                    Planet_1 + " (habitable) \n [2] Check Inventory  \n [3] Check Stats --> ")

        if planet_choice == "1":
            Event_pick = random.randint(1, 6)
            if Event_pick == 1:
                health = Planet1_event1(health)
            elif Event_pick == 2:
                Planet1_event2()
            elif Event_pick == 3:
                health, skill_warfare = Planet1_event3(health, skill_warfare)
                skill_warfare += 1
            elif Event_pick == 4:
                Planet1_event4()
            elif Event_pick == 5:
                Planet1_event5()
                health -= 15
            else:
                health, skill_warfare = Planet1_event6(health, skill_warfare)

        elif planet_choice == "2":
            typingPrint("\n")
            printinventory()
            typingPrint("You have " + equipped + " equipped.")
            equipped_choice = typingInput(
                "\n [1] Equip Item \n [2] Use health item \n [3] back --> ")
            if equipped_choice == "1":
                pick = typingInput("what would you like to equip? --> ")
                if pick in inventory:
                    equipped = str(pick)
                    typingPrint("you equipped " + equipped + ".")
                else:
                    typingPrint("You dont have that item")
                if equipped == "small stim" and "stim" and "large stim":
                    print("You fucking idiot")
            elif equipped_choice == "2":
                pick = typingInput("What would you like to use? --> ")
                if pick in inventory:
                    if pick == "small stim":
                        health += 20
                        inventory.remove("small stim")
                    elif pick == "stim":
                        health += 40
                        inventory.remove("stim")
                    elif pick == "large stim":
                        health += 60
                        inventory.remove("large stim")
            elif equipped_choice == "3":
                continue
        elif planet_choice == "3":
            typingPrint("\n\n You're current skills are: \n Pilot:" + str(skill_pilot) + "\n Mechanical:" +
                        str(skill_mechanic) + "\n Warfare:" + str(skill_warfare) + "\n Health:" + str(health) + "\n\n")
        else:
            typingPrint("TRY AGAIN")
###        Game over      ###
