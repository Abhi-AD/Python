# # # user input data in the user details

#-----------------------------------------------------------------------------------
#                    Single inheitance
#----------------------------------------------------------------------------------
class Data:
    
    def __init__(self):
        self.name = input("Please enter your name: ")
        self.age = int(input("Please enter your age: "))
        self.address = input("Please enter your address: ")
        
    
class Profile(Data):
    
    def profile(self):
        print(f"Hello i am a  {self.name}. I am a {self.age} years old. I am from {self.address}")
        
object = Profile()

object.profile()