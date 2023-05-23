# Programmed by: Rebekah Joy E. Sevial
# Error for UI and Class Calculator

# Create class named Error
class Error:
    # Define function to print error when ValueError
    def value_and_type_error(self):
        print("\n\033[31mError! You enter an invalid value! Please try again.\n")    
    # Define function to print error when invalid input
    def invalid_error(self):
        print("\n","\033[31mInvalid input!")
    # Define function to print error when ZeroDivisionError
    def zero_division_error(self):
        print("\n\033[31mError! You are dividing by zero.")