import re

email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email = input("Enter your email address: ")
if re.search(email_condition, user_email):
    print("Valid email address: ", user_email)
else:
    print("Invalid email address")
