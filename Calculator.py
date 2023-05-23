# Programmed by: Rebekah Joy E. Sevial
# Creating App Calculator using OOP

# Import the Calculator class from class_calculator file
from class_calculator import Calculator
# Import the UserInterface class from user_interface file
from user_interface import UserInterface
# Import the Error class of class_from_errors file
from class_for_errors import Error
# Create object for the three class
calcu = Calculator()
ui = UserInterface()
error = Error()
# Start
# Display the greetings to the user
ui.greet()
# Display the four operators of Calculator
ui.display_operations()
# Asks the user to decide which operation to use assigned from numbers 1 to 4
# Use the try and except function to check for the errors
while True:
    try: 
        operation = ui.ask_operator()
    except(ValueError, TypeError):
        error.value_and_type_error()

    if operation <= 4:
        try:
            num1 = ui.ask_number1()
            num2 = ui.ask_number2()
        except(ValueError, TypeError):
            error.value_and_type_error() 

    if operation == 1:
        sum = calcu.add(num1,num2)
        ui.print_sum(sum)
    elif operation == 2:
        difference = calcu.subtract(num1, num2)
        ui.print_difference(difference)
    elif operation == 3:
        product = calcu.multiply(num1, num2)
        ui.print_product(product)
    elif operation == 4:
        try:
            quotient = calcu.divide(num1, num2)
            ui.print_quotient(product)
        except ZeroDivisionError:
            error.zero_division_error()
    else:
        error.invalid_error()     
# Add a condition when the user inputted an invalid number
                
# Call for the function display menu