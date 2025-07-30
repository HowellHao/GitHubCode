def find_max(numbers):
    if not numbers:
        return "Empty List"
    max_numbers=numbers[0]
    for num in numbers:
        if num > max_numbers:
            max_numbers = num
    return max_numbers
while True:
    try:
        list_numbers = input("Insert List Number: ")
        list_numbers = [float(num) for num in list_numbers.split()]
        if not list_numbers:
            print("Empty list")
        else:
            max = find_max(list_numbers)
            print("Max Number: ", max)
        break
    except ValueError:
        print("Invalid Input")
    
