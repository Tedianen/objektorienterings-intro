# Adventure game in space

# Define a list of items that the player can pick up
items = []

# Define a list of traps that the player can encounter
traps = ["laser beam", "exploding star", "black hole"]

# Define a list of monsters that the player can encounter
monsters = ["alien", "robot", "zombie"]

# Define a function to print the player's inventory


def print_inventory():
    print("Inventory:")
    for item in items:
        print("- " + item)


# Define the main game loop
while True:
    # Print a message to the player
    print("You are lost in space, surrounded by dangers.")
    print("What do you want to do?")

    # Get the player's input
    action = input("> ")

    # Check if the player wants to pick up an item
    if action.lower() == "pick up":
        # Get the item the player wants to pick up
        item = input("What do you want to pick up?\n> ")
        # Add the item to the player's inventory
        items.append(item)
        print("You picked up a " + item)
    # Check if the player wants to check their inventory
    elif action.lower() == "inventory":
        print_inventory()
    # Check if the player wants to use an item
    elif action.lower() == "use":
        # Get the item the player wants to use
        item = input("What do you want to use?\n> ")
        # Check if the item is in the player's inventory
        if item in items:
            # Remove the item from the player's inventory
            items.remove(item)
            print("You used the " + item)
        else:
            print("You don't have that item.")
    # Check if the player has encountered a trap
    elif action.lower() in traps:
        print("You encountered a " + action + "! Be careful!")
    # Check if the player has encountered a monster
    elif action.lower() in monsters:
        print("You encountered a " + action + "! Defend yourself!")
    # If none of the above conditions are met, print an error message
    else:
        print("I'm sorry, I don't understand what you mean.")
