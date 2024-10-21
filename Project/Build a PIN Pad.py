def get_user_input(message):
     try:
          if message:
               return int(input(message))  
          else:
               return int(input())
     except ValueError:
          print("Invalid input. Please enter a number.")
     return None

def pin_pad():
    correct_pin = 1234  # Replace this with your desired PIN
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        entered_pin = get_user_input("Enter your 4-digit PIN: ")

        if entered_pin is not None:
            if entered_pin == correct_pin:
               print("PIN accepted. Access granted.")
               return True
            else:
               print(f"Invalid PIN. {max_attempts - attempts - 1} attempts left.")
               attempts += 1
               print(attempts)

    print("Too many failed attempts. Access denied.")
    return False

if __name__ == "__main__":
    print("Welcome to the PIN Pad!")
    access_granted = pin_pad()

    if access_granted:
     # Your code for granting access goes here
     print("Accessing the secured area...")
else:
     # Your code for denying access goes here
     print("Exiting the program...")
