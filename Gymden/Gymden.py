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


Planet_name = ["Bacu", "Ulu", "Html", "Ga",
               "Dagu", "kua", "los", "pollos", "hermanos"]

inventory = ["wrench"]


def print_inventory():
    print("Inventory:")
    for item in inventory:
        print("- " + item)


common_items = ["combat knife", "9mm revolver"]

rare_items = ["blaster", "a fucking pencil"]

epic_items = ["Plasma Thrower", "pulse rifle"]

legendary_item = ["comically small revolver", "BFG 9000"]

Mythical_item = ["comically large spoon"]

# Inventory Function


# Events for planet one

# Event 1

print("artin")


def Planet1_event1():
    plan = typingInput(
        "As you are decending towards sed planetuas the ship is hot. \n What is your plan of action? \n[1] Eavasiv Manuvers \n[2] Override the engine \n[3] Shoot the control panel")
    if plan == "1":
        difficulty = random.randint(1, 20) + int(skill_pilot)
        if difficulty >= 15:
            typingPrint(
                "You succsesfully managed to control the ship into a safe decent and landed without any mayor issues")

        elif difficulty >= 10:
            typingPrint(
                "You managed to control the ship with your skills, but you didnt come out of it unscaved \n You lost: 10 health")
            health = health - 10
        else:
            typingPrint("Wasted!")
            health = health - health
    elif plan == "2":
        difficulty = random.randint(1, 20) + int(skill_mechanic)
        if difficulty >= 15:
            typingPrint(
                "You managed to perfectly override the engine not putting out to much powa or to little poWAAA")
        elif difficulty >= 10:
            typingPrint(
                "You managed to override the engine but you put to much power in it causing you a major concussion")
            health = health - 10
        else:
            typingPrint("you ded")
    elif plan == "3":
        difficulty = random.randint(1, 20) + int(skill_warfare)
        if difficulty >= 15:
            typingPrint(
                "You shoot the control panel right in the center causing safe mode to activate and saving your sorrow ass. ")
            health = health - 50
        elif difficulty >= 10:
            typingPrint(
                "You shoot the control panel right in the center causing the ship to deactivate their thursters leading to ded.")
            health = health - health
        else:
            typingPrint(
                "you shoot the control panel causing it to explode in you face.")

# Loot generator


def Loot_event():
    typingPrint("you do be landing tho and locate chest")
    item_chance = random.randint(1, 100)

    if item_chance <= 40:
        item_chance = random.randint(1, 2)
        if item_chance <= 1:
            print("You have found a combat knife (Common) in the chest, congrats.")
        else:
            print("You have found a 9mm revolver (Common), please use with care.")
    elif item_chance <= 60:
        item_chance = random.randint(1, 2)
        if item_chance <= 1:
            print("You have located a blaster (Rare).")
        else:
            print("You have aqquired a fucking pencil (Rare). ")

    elif item_chance <= 75:
        item_chance = random.randint(1, 2)
        if item_chance <= 1:
            print("You have located a plasma thrower (Epic). ")
        else:
            print("You have found a pulse rifle (thats Epic). ")
    elif item_chance <= 90:
        item_chance = random.randint(1, 2)
        if item_chance <= 1:
            print("You have located a comically smal revolver (Legendary).")
        else:
            print("You have found a BFG 9000 (Legen wait for it... dary). ")
    elif item_chance <= 100:
        print("You scoop out a comically large spoon (Mythical).")

# def planet1 event2():
#     plan = input(
#         "As you are decending towards sed planetuas the ship is hot. \n What is your plan of action? \n[1] Eavasiv Manuvers \n[2] Override the engine \n[3] Shoot the control panel")
#     if plan == "1":
#         SUC = random.randint(1, 20) + int(skill_pilot)
#         if SUC >= 15:
#             print("You succsesfully managed to control the ship into a safe decent and landed without any mayor issues")

#         elif SUC >= 10:
#             print(
#                 "You managed to control the ship with your skills, but you didnt come out of it unscaved")
#             health = health - 10
#         else:
#             print("U DEAD!")
#             health = health - health
#     elif plan == "2":
#         SUC = random.randint(1, 20) + int(skill_mechanic)
#         if SUC >= 15:
#             print(
#                 "You managed to perfectly override the engine not putting out to much powa or to little poWAAA")
#         elif SUC >= 10:
#             print("You managed to override the engine but you put to much power in it causing you a major concussion")
#             health = health - 10
#         else:
#             print("you ded")
#     elif plan == "3":
#         SUC = random.randint(1, 20) + int(skill_warfare)
#         if SUC >= 15:
#             print("You shoot the control panel right in the center causing safe mode to activate and saving your sorrow ass. ")
#             health - 50
#         elif SUC >= 10:
#             print("You shoot the control panel right in the center causing the ship to deactivate their thursters leading to ded.")
#             health - health
#         else:
#             print("you shoot the control panel causing it to explode in you face.")


Start = typingInput("Do you want to play the game y/n? --> ")

if Start == ("yes"):
    typingPrint("good")
else:
    typingPrint("Yes you do ")


player_name = input("\n Enter your name here --> ")

W = typingInput("Welcome " + player_name +
                ",\nWe will now randomize your capabilities, press ENTER to continue. -->")

health = 100

skill_pilot = random.randint(7, 8)
skill_mechanic = random.randint(1, 20)
skill_warfare = random.randint(1, 20)

typingPrint("Your skills are:\n Piloting: " + str(skill_pilot) + "\n mechanical: " +
            str(skill_mechanic) + "\n Warfare: " + str(skill_warfare) + " ")

while health >= 0:
    if health <= 0:
        typingPrint("GAME OVER")
        break
    else:
        Planet_1 = "Ga"
        Planet_2 = "dagu"
        Planet_3 = "kua"

        planet_choice = typingInput("\n\n wich of the following planets would you like to explore for supplies?" "\n [1] " +
                                    Planet_1 + " (habitable) \n [2] " + Planet_2 + " (Terrestial) \n [3] " + Planet_3 + " (desolate rock)\n [4] Check Inventory  \n [5] Check Stats -->")

        if planet_choice == "1":
            Event_pick = random.randint(1, 1)
            if Event_pick == 1:
                Planet1_event1()

        elif planet_choice == "2":
            typingPrint("nej")

        elif planet_choice == "3":
            typingPrint("icke")

        elif planet_choice == "4":
            typingPrint()

        elif planet_choice == "5":
            typingPrint("\n\n You're current skills are: \n Pilot:" + str(skill_pilot) + "\n Mechanical:" +
                        str(skill_mechanic) + "\n Warfare:" + str(skill_warfare) + "\n Health:" + str(health) + "\n\n")
        else:
            typingPrint("TRY AGAIN")
