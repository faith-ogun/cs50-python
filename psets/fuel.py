while True:
    try:
        fraction = input("Fraction: ")
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)

        if x > y:
            continue # Do not use fraction to try and reprompt the user as that will do nothing
            # continue is basically like ask again
        else:
            total = x / y

    except (ValueError, ZeroDivisionError):
        pass # or continue

    else:
        break

if total <= 0.01:
    print("E")
elif total >= 0.99:
    print("F")
else:
    print(f"{total * 100:.0f}%")