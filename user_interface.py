# Programmed by: Rebekah Joy E. Sevial
# User Interface for App Calculator

# Create a class named UserInterface
class UserInterface:
# Define function to greet the user 
    def greet(self):
        print("\033[0;33m===========================================")
        print("\033[0;33m             " + "\033[0;33m\033[1mSIMPLE CALCULATOR\033[0m" + "\033[0;33m             ")
        print("\033[0;33m===========================================" + "\n")
# Define function to display the operators of the Calculator
    def display_operators(self):
        print("\n\033[36mWhat operation do you like to do?\n")
        print("\033[36m1. Addition")
        print("\033[36m2. Subtraction")
        print("\033[36m3. Multiplication")
        print("\033[36m4. Division")       
# Define function that will ask the user which operation to use from number 1 to 4
# Define function to check if the chosen operator is existing from 1 to 4
# Define function that will ask the user to input two numbers
# Define function to execute the chosen operator
# Define function to print the output
# Define function to ask the user if he/she wants to retry