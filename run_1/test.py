import requests

def test_addition_operation():
    print("Test Case 1: Test addition operation")
    url = "http://localhost:5000/calculate?operation=add&num1=2&num2=3"
    response = requests.get(url)
    print("Expected status code: 200")
    print("Actual status code: ", response.status_code)
    print("Expected result: 5")
    print("Actual result: ", response.text)

def test_division_operation_with_invalid_input():
    print("\nTest Case 2: Test division operation with invalid input")
    url = "http://localhost:5000/calculate?operation=divide&num1=10&num2=0"
    response = requests.get(url)
    print("Expected status code: 400")
    print("Actual status code: ", response.status_code)
    print("Expected error message: 'Cannot divide by zero'")
    print("Actual error message: ", response.text)

def main():
    print("Starting the test cases for the calculation app")
    test_addition_operation()
    test_division_operation_with_invalid_input()
    print("All test cases completed")