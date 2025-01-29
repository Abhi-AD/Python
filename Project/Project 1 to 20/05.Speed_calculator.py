from time import time
import random as r


def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error += 1
        except:
            error += 1
    return error


def speed_time(time_start, time_end, testinput):
    elapsed_time = round((time_end - time_start), 2)
    speed = len(testinput) / elapsed_time
    return round(speed)


if __name__ == "__main__":
    while True:
        chk = input("Ready to Test? (yes/y or no/n): ").strip().lower()
        if chk in ["yes", "y"]:
            test = [
                "A paragraph is a self-contained unit of discourse in writing dealing with a particular point or idea.",
                "My name is Abhishek Dangi.",
                "Welcome to Abhi-AD!",
            ]
            test1 = r.choice(test)
            print("\nTyping Speed Test...")
            print(test1)
            print("\n")

            time_start = time()
            testinput = input("Enter: ")
            time_end = time()

            print("\nSpeed:", speed_time(time_start, time_end, testinput), "W/S")
            print("Errors:", mistake(test1, testinput))
        elif chk in ["no", "n"]:
            print("Thanks for playing!")
            break
        else:
            print(
                "Invalid input. Please enter 'yes' or 'y' to start, and 'no' or 'n' to exit."
            )
