# history.py

# In-memory database to store the history of calculations
calculation_history = {}

def add_to_history(calculation_id, operation, inputs, result):
    """
    Add a calculation to the history.
    """
    calculation_history[calculation_id] = {
        'operation': operation,
        'inputs': inputs,
        'result': result
    }
    print(f"Calculation {calculation_id} added to history.")

def get_history():
    """
    Retrieve the history of calculations.
    """
    print("Retrieving calculation history...")
    return calculation_history

def clear_history():
    """
    Clear the history of calculations.
    """
    calculation_history.clear()
    print("Calculation history cleared.")