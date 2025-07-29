try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Error: Division by zero is not allowed.")
    print(f"Exception message: {e}")
else:
    print("Division successful, result is:", result)
finally:
    print("Execution completed, whether an exception occurred or not.")
    print("This block always executes.")