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
