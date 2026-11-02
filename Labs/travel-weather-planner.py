def calculate_check_digit_10(isbn):
    total = sum(int(isbn[i]) * (10 - i) for i in range(9))
    remainder = total % 11
    check_digit = (11 - remainder) % 11
    return 'X' if check_digit == 10 else str(check_digit)


def calculate_check_digit_13(isbn):
    total = sum(
        int(isbn[i]) * (1 if i % 2 == 0 else 3)
        for i in range(12)
    )
    return str((10 - total % 10) % 10)


def validate_isbn(isbn, length):
    if length not in (10, 13):
        return "Length should be 10 or 13."

    if len(isbn) != length:
        return f"ISBN-{length} code should be {length} digits long."

    try:
        if length == 10:
            for digit in isbn[:9]:
                int(digit)
            expected = calculate_check_digit_10(isbn)
            return "Valid ISBN Code." if isbn[-1] == expected else "Invalid ISBN Code."

        if length == 13:
            for digit in isbn[:12]:
                int(digit)
            int(isbn[-1])
            expected = calculate_check_digit_13(isbn)
            return "Valid ISBN Code." if isbn[-1] == expected else "Invalid ISBN Code."

    except ValueError:
        return "Invalid character was found."


def main():
    user_input = input("Enter ISBN and length: ")

    try:
        values = user_input.split(",")
        isbn = values[0].strip()
        length = int(values[1].strip())
    except IndexError:
        print("Enter comma-separated values.")
        return
    except ValueError:
        print("Length must be a number.")
        return

    print(validate_isbn(isbn, length))


main()