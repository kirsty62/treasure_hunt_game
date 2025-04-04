import time
import random

# Define treasure rewards based on the chosen box
treasure_boxes = {
    "bronze": ["Diamond Ring 💍", "Pearl Bracelet 📿"],
    "gold": ["OOPS, NOTHING HERE!! 😢"],
    "silver": ["Ruby Pendant 💎"],
    "brass": ["2 Golden Bars 🏆🏆"],
    "black": ["Precious Key to the King's House 🔑👑"]
}

# Player's collected treasures
collected_treasures = []

# Function to validate user input
def get_valid_input(prompt, valid_options):
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_options:
            return user_input
        print("Invalid input. Please try again!")

# Introduction
print("🎮 Welcome to the TREASURE HUNT game! 🎮")
time.sleep(1)
print("You find yourself in a dark hallway with two doors...")
time.sleep(1)

# Choose a magical artifact
print("\nBefore you enter, you find three magical artifacts:")
print("1️⃣ A golden shield 🛡️ (Protects from lions)")
print("2️⃣ A flying cape 🦸 (Lets you fly over the river)")


artifact = get_valid_input("Which one do you pick? (shield/cape): ", ["shield", "cape"])

# Choosing the door
print("\nThere are two doors in front of you: ")
print("🔴 Red Door - Enter at your own risk!!🦁")
print("🔵 Blue Door - Looks mysterious 💎")

door_choice = get_valid_input("Which door do you choose? (red/blue): ", ["red", "blue"])

if door_choice == "red":
    print("\nYou enter the Red Door... 🦁")
    time.sleep(1)
    print("Oh no! It's full of hungry lions! 🦁🔥")
    
    if artifact == "shield":
        print("Your golden shield protects you! You escape safely! 🛡️🏃")
        print("You run back and enter the BLUE door instead...")
        door_choice = "blue"
    else:
        print("GAME OVER! The lions got you! 💀")
        exit()

if door_choice == "blue":
    print("\nYou enter the Blue Door... 💎")
    time.sleep(1)
    print("WOW! It's a room full of treasure! 🏆💰✨")

    # Choosing 3 treasure boxes from 5
    print("\nThere are five treasure boxes in this room for you:")
    print("📦 Bronze Box")
    print("📦 Gold Box")
    print("📦 Silver Box")
    print("📦 Brass Box")
    print("📦 Black Box")

    chosen_boxes = []  # Store selected boxes
    while len(chosen_boxes) < 3:
        box_choice = get_valid_input("Pick a treasure box (bronze/gold/silver/brass/black): ", 
                                     ["bronze", "gold", "silver", "brass", "black"])

        if box_choice in chosen_boxes:
            print("You already picked this box! Choose a different one.")
            continue

        chosen_boxes.append(box_choice)
        treasures = treasure_boxes[box_choice]  # Get treasures from chosen box
        print(f"🎁 You opened the {box_choice.capitalize()} Box and found: {', '.join(treasures)}")
        collected_treasures.extend(treasures)

        if len(chosen_boxes) < 3:
            print("✅ Proceed and pick another one!")

    print("\nEnough hunting for today!! 🎯 Time to move on!")

    time.sleep(1)
    print("\nAfter collecting your treasure, you encounter a river! 🌊")
    print("Do you want to try and cross the river or stay?")

    river_choice = get_valid_input("Type 'cross' to cross the river, or 'stay' to stay: ", ["cross", "stay"])

    if river_choice == "cross":
        print("\nYou try to cross the river... 🌊💦")
        time.sleep(1)

        if artifact == "cape":
            print("Your flying cape lifts you above the river! 🦸‍♂️✨")
            print("You fly over safely and escape with the treasure! 🎉🏆 YOU WIN!")
        else:
            print("Oh no! The river is too deep, and you sink! 💀 GAME OVER!")
            exit()
    elif river_choice == "stay":
        print("\nYou decide not to cross the river... 🚶‍♂️")
        time.sleep(1)
        print("A secret exit appears behind you! 🏆")
        print("Congratulations! YOU WIN! 🎉🎊")

# Display collected treasures at the end
print("\n🛍️ You collected the following treasures:")
for item in collected_treasures:
    print(f"- {item}")

print("\nThanks for playing TREASURE HUNT! 🎮")

