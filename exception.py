
# Define a function to divide two numbers
def divide_numbers(num1, num2):
    try:
        # Attempt to divide the numbers
        result = num1 / num2
        print(f"The result is: {result}")

    except ZeroDivisionError:
        # Handle division by zero error
        print("Error: Cannot divide by zero!")

    except TypeError:
        # Handle type mismatch error
        print("Error: Invalid input type. Please enter numbers only.")

    except ValueError:
        # Handle value error
        print("Error: Invalid input value. Please enter a valid number.")

    except Exception as e:
        # Catch any other unexpected exceptions
        print(f"An unexpected error occurred: {e}")


# Test 1: Valid inputs
print("Test 1: Valid inputs")
divide_numbers(10, 2)

# Test 2: Division by zero
print("\nTest 2: Division by zero")
divide_numbers(10, 0)

# Test 3: Invalid input types
print("\nTest 3: Invalid input types")
divide_numbers("ten", 2)

# Test 4: Value error
print("\nTest 4: Value error")
divide_numbers(10, "two")

# Test 5: Unexpected exception
print("\nTest 5: Unexpected exception")
divide_numbers(10, None)