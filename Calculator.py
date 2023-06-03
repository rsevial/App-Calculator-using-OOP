# Programmed by: Rebekah Joy E. Sevial
# Creating App Calculator using OOP

# Import the Calculator class from class_calculator file
from class_calculator import Calculator
# Import the UserInterface class from user_interface file
from user_interface import UserInterface
# Import the Error class of class_from_errors file
from class_for_errors import Error
# Import the NewUserInterface of new_class file
from new_class import NewUserInterface

# Create object for the three class
calcu = Calculator()
ui = UserInterface()
error = Error()
new_ui = NewUserInterface()
# Start
# Display the greetings to the user
ui.greet()
# Display the four operators of Calculator
ui.display_operations()
# Use While lopp and Asks the user to decide which operation to use assigned from numbers 1 to 4
# Use the try and except function to check for the errors
while True:
    try: 
        operation = ui.ask_operator()
    except(ValueError, TypeError):
        error.value_and_type_error()
        continue
    # Add condition to check if the user inputted valid numbers
    # If operation <= 4: ask user for num1 and num2
    # Use try and except function if the user inputted invalid numbers
    if operation <= 4:
        try:
            num1 = ui.ask_number1()
            num2 = ui.ask_number2()
        except(ValueError, TypeError):
            error.value_and_type_error() 
    # print sum if the user choose 1
    if operation == 1:
        sum = calcu.add(num1,num2)
        ui.print_sum(sum)
    # print difference if the user choose 2
    elif operation == 2:
        difference = calcu.subtract(num1, num2)
        ui.print_difference(difference)
    # print product if the user choose 3
    elif operation == 3:
        product = calcu.multiply(num1, num2)
        ui.print_product(product)
    # print quotient if the user choose 4
    elif operation == 4:
        try:
            quotient = calcu.divide(num1, num2)
            ui.print_quotient(quotient)
        # except if the num2 == 0: use except ZeroDivisionError
        except ZeroDivisionError:
            error.zero_division_error()
    else:
        error.invalid_error()

# Elif statement that will ask the user again if he/she wants to retry
    # If not ui.retry: break
    if not new_ui.retry():
        break
    # else: diplay operations and continue
    else:
        ui.retry
        ui.display_operations()
        continue  