def check_SIN(sin):
    """
    Check if the provided SIN (Social Insurance Number) is valid.
    
    :param sin: A string representing the SIN to be checked.
    :return: True if the SIN is valid, False otherwise.
    """
    if len(sin) != 9 or not sin.isdigit():
        return False

    digits = [int(digit) for digit in sin]
    # Apply the Luhn algorithm
    for i in range(0, len(digits) - 1, 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    # Sum the digits and check if the last digit is valid
    last_digit = digits.pop()
    digits_sum = sum(digits)
    digits.append(last_digit)
    digits_sum += last_digit
    # The SIN is valid if the sum of the digits is divisible by 10
    if digits_sum % 10 != 0:
        return False
    return True

def main():
    sin = input("Enter the SIN to check: ")
    
    if check_SIN(sin):
        print(f"The SIN {sin} is valid.")
    else:
        print(f"The SIN {sin} is invalid.")
if __name__ == "__main__":
    main()