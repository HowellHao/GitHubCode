def check_SIN(sin):
    """
    Check if a given Social Insurance Number (SIN) is valid.

    :param sin: A string representing the SIN to be checked.
    :return: True if the SIN is valid, False otherwise.
    """
    if not isinstance(sin, str) or len(sin) != 9 or not sin.isdigit():
        return False

    # Convert the SIN into a list of integers
    digits = [int(digit) for digit in sin]

    # Luhn algorithm implementation
    for i in range(1, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9

    return sum(digits) % 10 == 0
def main():
    sin = input("Enter a Social Insurance Number (SIN): ")
    if check_SIN(sin):
        print(f"The SIN {sin} is valid.")
    else:
        print(f"The SIN {sin} is invalid.")
if __name__ == "__main__":
    main()