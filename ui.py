# Import necessary modules
from calculation_engine import add, subtract, multiply, divide, exponentiation, square_root, logarithm, validate_input
from history import add_to_history, get_history, clear_history

def display_menu():
    """
    Function to display the menu to the user
    """
    print("\nWelcome to the Calculation App!")
    print("Please select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiation")
    print("6. Square Root")
    print("7. Logarithm")
    print("8. View Calculation History")
    print("9. Clear Calculation History")
    print("0. Exit")
    print("\n")

def get_user_input():
    """
    Function to get the user's input
    """
    try:
        choice = int(input("Enter your choice: "))
        print("You selected: ", choice)
        return choice
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

def get_numbers():
    """
    Function to get the numbers from the user
    """
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("You entered: ", num1, " and ", num2)
        return num1, num2
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None, None

def display_result(result):
    """
    Function to display the result to the user
    """
    print("The result is: ", result)

def display_error(message):
    """
    Function to display an error message to the user
    """
    print("Error: ", message)

def display_history():
    """
    Function to display the calculation history to the user
    """
    history = get_history()
    if history:
        print("Calculation History:")
        for calculation_id, calculation in history.items():
            print(f"ID: {calculation_id}, Operation: {calculation['operation']}, Inputs: {calculation['inputs']}, Result: {calculation['result']}")
    else:
        print("No calculations in history.")

def clear_calculation_history():
    """
    Function to clear the calculation history
    """
    clear_history()
    print("Calculation history cleared.")