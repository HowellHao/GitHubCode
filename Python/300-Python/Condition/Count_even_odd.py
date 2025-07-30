def count_even_odd(numbers):
    even_count = 0
    odd_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count
try:
    list_number = input("Insert Number: ")
    numbers = [int(num) for num in list_number.split()]
    even_count, odd_count = count_even_odd(numbers)
    print(f"Even numbers: {even_count}, Odd numbers: {odd_count}")
except ValueError:
    print("Invalid input. Please enter a list of numbers separated by space.")
    