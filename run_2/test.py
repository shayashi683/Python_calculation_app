import requests

def test_addition_operation():
    print("Test Case 1: Test addition operation")
    url = "http://localhost:5000/calculate?operation=add&num1=2&num2=3"
    response = requests.get(url)
    print("Expected status code: 200")
    print("Actual status code: ", response.status_code)
    print("Expected result: 5")
    print("Actual result: ", response.text)
    assert response.status_code == 200, "Status code does not match expected value"
    assert response.text == '5', "Result does not match expected value"

def test_division_operation_with_invalid_input():
    print("\nTest Case 2: Test division operation with invalid input")
    url = "http://localhost:5000/calculate?operation=divide&num1=10&num2=0"
    response = requests.get(url)
    print("Expected status code: 400")
    print("Actual status code: ", response.status_code)
    print("Expected error message: 'Cannot divide by zero'")
    print("Actual error message: ", response.text)
    assert response.status_code == 400, "Status code does not match expected value"
    assert response.text == 'Cannot divide by zero', "Error message does not match expected value"

def main():
    test_addition_operation()
    test_division_operation_with_invalid_input()