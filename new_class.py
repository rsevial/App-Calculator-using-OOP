# Programmed by: Rebekah Joy E. Sevial
# Create a new class that inherits from existing class in your calculator program

# import a class from files
from user_interface import UserInterface
# create new class from the imported class
class NewUserInterface(UserInterface):
# add new methods
    def greetings(self):
        print("Thank you for using the calculator!")
# override an existing methods
    def retry(self):
        retry =  input("\n\033[35mDo you still want to continue? (y/n): ")
        if retry.lower() == "y":
            return True
        elif retry.lower() == "n":
            return False 
        else:
            print("\n\033[31mInvalid input!")