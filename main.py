import calculation_engine as ce
import history as hist
import ui

def main():
    while True:
        ui.display_menu()
        user_choice = ui.get_user_input("Enter your choice: ")

        if user_choice == '1':
            num1 = ui.get_user_input("Enter first number: ")
            num2 = ui.get_user_input("Enter second number: ")
            result = ce.add(num1, num2)
            ui.display_result(result)
            hist.add_to_history('add', [num1, num2], result)
            print("Added calculation to history.")
        elif user_choice == '2':
            num1 = ui.get_user_input("Enter first number: ")
            num2 = ui.get_user_input("Enter second number: ")
            result = ce.subtract(num1, num2)
            ui.display_result(result)
            hist.add_to_history('subtract', [num1, num2], result)
            print("Added calculation to history.")
        elif user_choice == '3':
            num1 = ui.get_user_input("Enter first number: ")
            num2 = ui.get_user_input("Enter second number: ")
            result = ce.multiply(num1, num2)
            ui.display_result(result)
            hist.add_to_history('multiply', [num1, num2], result)
            print("Added calculation to history.")
        elif user_choice == '4':
            num1 = ui.get_user_input("Enter first number: ")
            num2 = ui.get_user_input("Enter second number: ")
            result = ce.divide(num1, num2)
            ui.display_result(result)
            hist.add_to_history('divide', [num1, num2], result)
            print("Added calculation to history.")
        elif user_choice == '5':
            num = ui.get_user_input("Enter number: ")
            result = ce.square_root(num)
            ui.display_result(result)
            hist.add_to_history('square_root', [num], result)
            print("Added calculation to history.")
        elif user_choice == '6':
            num = ui.get_user_input("Enter number: ")
            result = ce.logarithm(num)
            ui.display_result(result)
            hist.add_to_history('logarithm', [num], result)
            print("Added calculation to history.")
        elif user_choice == '7':
            history = hist.get_history()
            ui.display_history(history)
        elif user_choice == '8':
            hist.clear_history()
            print("Cleared calculation history.")
        elif user_choice == '9':
            print("Exiting the application.")
            break
        else:
            ui.display_error("Invalid choice. Please try again.")