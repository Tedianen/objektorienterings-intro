import random


Planet_name = ["Bacu", "Ulu", "Html", "Ga", "Dagu", "kua"]

# Events for planet one

# Event 1


def Planet1_event1():
    plan = input(
        "As you are decending towards sed planetuas the ship is hot. \n What is your plan of action? \n[1] Eavasiv Manuvers \n[2] Override the engine \n[3] Shoot the control panel")
    if plan == "1":
        difficulty = random.randint(1, 20) + int(skill_pilot)
        if difficulty >= 15:
            print("You succsesfully managed to control the ship into a safe decent and landed without any mayor issues")

        elif difficulty >= 10:
            print(
                "You managed to control the ship with your skills, but you didnt come out of it unscaved \n You lost: 10 health")
            health = health - 10
        else:
            print("Wasted!")
            health = health - health
    elif plan == "2":
        difficulty = random.randint(1, 20) + int(skill_mechanic)
        if difficulty >= 15:
            print(
                "You managed to perfectly override the engine not putting out to much powa or to little poWAAA")
        elif difficulty >= 10:
            print("You managed to override the engine but you put to much power in it causing you a major concussion")
            health = health - 10
        else:
            print("you ded")
    elif plan == "3":
        difficulty = random.randint(1, 20) + int(skill_warfare)
        if difficulty >= 15:
            print("You shoot the control panel right in the center causing safe mode to activate and saving your sorrow ass. ")
            health = health - 50
        elif difficulty >= 10:
            print("You shoot the control panel right in the center causing the ship to deactivate their thursters leading to ded.")
            health = health - health
        else:
            print("you shoot the control panel causing it to explode in you face.")


# def två():
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


Start = input("Do you want to play the game y/n? --> ")

if Start == ("yes"):
    print("good")
else:
    print("Yes you do")


player_name = input("Enter your name here --> ")

W = input("Welcome " + player_name +
          ". We will now randomize your capabilities, press ENTER to continue. -->")

health = 100

skill_pilot = random.randint(7, 8)
skill_mechanic = random.randint(1, 20)
skill_warfare = random.randint(1, 20)

print("Your skills are:\n Piloting: " + str(skill_pilot) + "\n mechanical: " +
      str(skill_mechanic) + "\n Warfare: " + str(skill_warfare) + " ")

while health >= 0:
    if health <= 0:
        print("GAME OVER")
        break
    else:
        Planet_1 = "Ga"
        Planet_2 = "dagu"
        Planet_3 = "kua"

        planet_choice = input("wich of the following planets would you like to explore for supplies?" "\n [1] " +
                              Planet_1 + " (habitable) \n [2] " + Planet_2 + " (Terrestial) \n [3] " + Planet_3 + " (desolate rock)\n -->")

        if planet_choice == "1":
            Event_pick = random.randint(1, 1)
            if Event_pick == 1:
                Planet1_event1()

        elif planet_choice == "2":
            print("nej")

        elif planet_choice == "3":
            print("icke")
        else:
            print("TRY AGAIN")
