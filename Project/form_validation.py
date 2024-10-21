import json
import re

def is_valid_email(email):
    # Email validation using regular expression
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email)

def is_valid_name(name):
    # Name validation: Only allow alphabets and spaces
    return name.isalpha()

def is_valid_class(class_num):
    # Class validation: Allow integers between 1 and 12
    return 1 <= class_num <= 12

def is_valid_age(age):
    # Age validation: Require age to be 18 or above
    return 5<=age<=30

user_num = int(input("Enter a save data number: "))

for i in range(user_num):
    # Get user input for Name, Class, Age, and Email
    name = input("Enter Name: ")
    while not is_valid_name(name):
         print("Only use alphabets for the name!")
         name = input("Enter Name: ")
    class_num = int(input("Enter Class: "))
    while not is_valid_class(class_num):
         print("Only use integers between 1 and 12 for class.")
         class_num = int(input("Enter Class: "))
    age = int(input("Enter Age: "))
    while not is_valid_age(age):
         print("Please Enter Age of 18 or above.")
         age = int(input("Enter Age: "))
         
    
    # Validate the email input
    email = input("Enter your email: ")
    while not is_valid_email(email):
        print("Invalid email format. Please enter a valid email.")
        email = input("Enter your email: ")
  
    # Create a Python dictionary from the user input
    python_obj = {
        "Name": name,
        "Class": class_num,
        "Age": age,
        "Email": email
    }
  
    # Convert the Python dictionary to a JSON object
    json_obj = json.dumps(python_obj)
  
    # Print the JSON data
    print("\nJSON data for the dictionary:")
    print(json_obj)
  
    # Load the JSON object back into a Python object
    loaded_python_obj = json.loads(json_obj)
  
    # Print the data from the loaded Python object
    print("\nName:", loaded_python_obj["Name"])
    print("Class:", loaded_python_obj["Class"])
    print("Age:", loaded_python_obj["Age"])
    print("Email:", loaded_python_obj["Email"])
  
    # Check if the user is in class 10 and print a special message
    if class_num == 10:
        print("You are in Class 10! Enjoy your senior year!")
    else:
        print("Have a great time in your current class!")
