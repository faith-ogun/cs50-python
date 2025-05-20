def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Rule 1: Length between 2 and 6
    if len(s) < 2 or len(s) > 6:
        return False

    # Rule 2: Must start with at least two letters
    if s[0:2].isdigit():
        return False

    # Rule 3: No special characters (only letters and numbers)
    if not s.isalnum():
        return False

    # Rule 4 & 5: Numbers must be at the end, and first number can't be 0
    has_started_number = False
    for char in s:
        if char.isdigit():
            if not has_started_number:
                has_started_number = True
                if char == '0':
                    return False
        elif has_started_number:
            # If a letter appears after a number, invalid
            return False

    return True

main()
