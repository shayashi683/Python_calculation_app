# calculation_engine.py

import math
import logging

logging.basicConfig(level=logging.DEBUG)

def add(num1, num2):
    logging.info(f"Adding {num1} and {num2}")
    return num1 + num2

def subtract(num1, num2):
    logging.info(f"Subtracting {num2} from {num1}")
    return num1 - num2

def multiply(num1, num2):
    logging.info(f"Multiplying {num1} and {num2}")
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        logging.error("Cannot divide by zero")
        return "Error: Cannot divide by zero"
    logging.info(f"Dividing {num1} by {num2}")
    return num1 / num2

def exponentiation(base, exponent):
    logging.info(f"Raising {base} to the power of {exponent}")
    return base ** exponent

def square_root(num):
    if num < 0:
        logging.error("Cannot calculate the square root of a negative number")
        return "Error: Cannot calculate the square root of a negative number"
    logging.info(f"Calculating the square root of {num}")
    return math.sqrt(num)

def logarithm(num, base=math.e):
    if num <= 0:
        logging.error("Cannot calculate the logarithm of a non-positive number")
        return "Error: Cannot calculate the logarithm of a non-positive number"
    logging.info(f"Calculating the logarithm of {num} with base {base}")
    return math.log(num, base)

def validate_input(input_str):
    try:
        num = float(input_str)
        logging.info(f"Validated input: {num}")
        return num
    except ValueError:
        logging.error("Invalid input")
        return "Error: Invalid input"