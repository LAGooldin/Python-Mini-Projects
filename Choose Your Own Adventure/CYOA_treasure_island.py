import sys

print("Welcome to the Treasure Island Game. Your goal is to make it to the treasure island so you can find the treasure.\nEvery decision you make could determine your fate.")

# Initial Input for the Adventurer's Name
name = input("What is the adventurer's name? ")

while not name:
    print("No name was given. Please insert a valid name.")
    name = input("What is the adventurer's name? ")

print(f"\nGreetings, Adventurer {name}. Welcome to the quest for Treasure Island.")
print("Legend has it that the treasure of the ancient pirate, Captain Blackbeard, lies hidden on this mysterious island.\n")

# First Decision: Path Choice
left_right = input("You arrive at a fork in the road. One path is overgrown with thick vines and leads to the left, while the other is a well-trodden path to the right.\nWhich path do you choose? (left/right) ").strip().lower()

while not left_right:
    print("You did not make an input. The jungle's shadows seem to grow darker...")
    left_right = input("Which path do you choose? (left/right) ").strip().lower()

# Second Decision: Wait or Swim
if left_right == 'left':
    print("\nYou bravely choose the overgrown path, cutting through vines and pushing past branches.")
    wait_swim = input("After hours of trekking, you find yourself at the edge of a vast, shimmering lake. Do you want to wait for a boat or swim across? (wait/swim) ").strip().lower()

    while not wait_swim:
        print("You did not make a valid selection. The water ripples in the moonlight, awaiting your decision.")
        wait_swim = input("Do you want to wait for a boat or swim across? (wait/swim) ").strip().lower()

    if wait_swim == "wait":
        print("\nYou decide to wait patiently. As dawn breaks, a small boat appears on the horizon. A friendly fisherman offers you a ride to the other side.")
        door = input("On the other side, you find an ancient temple with three doors. Each door bears a different symbol: a skull, a crown, and a serpent. Which door do you choose? (1/skull, 2/crown, 3/serpent) ").strip().lower()

        # Third Decision: Door Choice
        while not door:
            print("You did not make a selection. The temple walls echo with distant whispers...")
            door = input("Which door do you choose? (1/skull, 2/crown, 3/serpent) ").strip().lower()

        if door == '1' or door == 'skull':
            sys.exit("The skull door creaks open, revealing a room filled with traps. You have met a grim end. Game Over.")
        elif door == '2' or door == 'crown':
            print("The crown door opens to a chamber filled with glittering gold and precious gems. You have found the treasure! Congratulations, Adventurer!")
        elif door == '3' or door == 'serpent':
            sys.exit("The serpent door hisses open, releasing a torrent of venomous snakes. You have met a swift end. Game Over.")

    elif wait_swim == "swim":
        sys.exit("You bravely dive into the lake, but the currents are too strong. You struggle and ultimately succumb to the watery depths. Game over.")

elif left_right == 'right':
    sys.exit("You choose the well-trodden path, but it leads straight into a den of hungry wolves. You have met a tragic end. Game over.")

print("\nThank you for playing!")
