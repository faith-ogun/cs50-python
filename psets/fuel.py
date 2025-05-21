# ----- First Iteration -----
# while True:
#     try:
#         fraction = input("Fraction: ")
#         x, y = fraction.split("/")
#         x = int(x)
#         y = int(y)
#
#         if x > y:
#             continue # Do not use fraction to try and reprompt the user as that will do nothing
#             # continue is basically like ask again
#         else:
#             total = x / y
#
#     except (ValueError, ZeroDivisionError):
#         pass # or continue
#
#     else:
#         break
#
# if total <= 0.01:
#     print("E")
# elif total >= 0.99:
#     print("F")
# else:
#     print(f"{total * 100:.0f}%")

# ----- Second Iteration -----
def main():
    while True:
        fraction = input("Fraction: ") # intializing to ensure fraction is defined.

        try:
            percentage = convert(fraction) # percentage is the returned total.
            break

        except (ValueError, ZeroDivisionError):
           continue

    print(gauge(percentage)) # uses same nomenclature as function

def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)

    if y == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    if x > y:
        raise ValueError("Improper fraction")

    return round((x / y) * 100)

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
