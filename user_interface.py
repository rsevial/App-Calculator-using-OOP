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
    def display_operations(self):
        print("\n\033[36mWhat operation do you like to do?\n")
        print("\033[36m1. Addition")
        print("\033[36m2. Subtraction")
        print("\033[36m3. Multiplication")
        print("\033[36m4. Division")       
# Define function that will ask the user which operation to use from number 1 to 4
    def ask_operator(self):
        user_choice = int(input("\n"+"\033[36mEnter your choice from 1 to 4: \033[33m"))
        return user_choice
# Define function that will ask the user to input two numbers
    def ask_number1(self):
        num1 = float(input("\033[36mEnter your first number: \033[33m"))
        return num1
    def ask_number2(self):
        num2 = float(input("\033[36mEnter your second number: \033[33m"))
        return num2          
# Define function to print the output
    # print sum
    def print_sum(self, sum):
        print ("Sum: " + str(sum))
    # print difference
    def print_difference(self, difference):
        print ("Difference: " + str(difference))
    # print product
    def print_product(self, product):
        print ("Product: " + str(product))
    # print quotient
    def print_quotient(self, quotient):
        print ("Quotient: " + str(quotient))
# Define function to ask the user if he/she wants to retry
    def retry(self):
        retry =  input("\n\033[35mDo you still want to continue? (y/n): ")
        if retry.lower() == "y":
            return True
        elif retry.lower() == "n":
            print("\033[36mThank you!")
            return False 
        else:
            print("\n\033[31mInvalid input!")
            return True