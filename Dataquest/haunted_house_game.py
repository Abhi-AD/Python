import random


def print_welcome():
    print("Welcome to the Haunted House Adventure Game!")
    print("Your goal is to survive and find the treasure hidden in the haunted house.")
    print("Good luck!\n")


def choose_room():
    print("\nYou're standing in a dimly lit hallway with three doors.")
    print("1. Enter the room to the left.")
    print("2. Enter the room in the center.")
    print("3. Enter the room to the right.")
    return input("Choose a room (1, 2, or 3): ")


def left_room():
    print("\nYou entered the left room and encountered a ghost!")
    choice = input("Do you want to (1) run away or (2) confront the ghost? ")
    if choice == "1":
        print("You ran back to the hallway, but the ghost follows you.")
        return False
    elif choice == "2":
        print(
            "You bravely confront the ghost, and it vanishes! You find a key on the floor."
        )
        return True
    else:
        print("Invalid choice, returning to the hallway.")
        return False


def center_room():
    print("\nYou entered the center room and found a treasure chest!")
    choice = input("Do you want to (1) open the chest or (2) leave it? ")
    if choice == "1":
        if random.choice([True, False]):
            print(
                "The chest was trapped! You fall through a trapdoor and are lost in the dark."
            )
            return False
        else:
            print("The chest contains the treasure! Congratulations, you win!")
            return True
    elif choice == "2":
        print("You leave the chest and return to the hallway.")
        return False
    else:
        print("Invalid choice, returning to the hallway.")
        return False


def right_room():
    print("\nYou entered the right room and find a sleeping vampire.")
    choice = input("Do you want to (1) sneak past it or (2) attack it? ")
    if choice == "1":
        print("You quietly sneak past the vampire and find an exit door!")
        return True
    elif choice == "2":
        print(
            "You try to attack the vampire, but it awakens and chases you back to the hallway."
        )
        return False
    else:
        print("Invalid choice, returning to the hallway.")
        return False


def main():
    print_welcome()
    while True:
        room_choice = choose_room()
        if room_choice == "1":
            if left_room():
                break
        elif room_choice == "2":
            if center_room():
                break
        elif room_choice == "3":
            if right_room():
                break
        else:
            print("Invalid choice. Please try again.")

    print("\nThank you for playing the Haunted House Adventure Game! Goodbye!")


# Run the game
main()
