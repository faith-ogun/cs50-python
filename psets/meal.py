def main():
    what_time = convert(input("What time is it? "))

# 'what_time == range(7, 8)' is incorrect because:
# 1. 'range(7, 8)' creates a range object (like [7]), not a float or number.
# 2. Comparing a float (e.g. 7.5) to a range directly with == always returns False.
# 3. Even if what_time == 7.0, it still won’t equal range(7, 8); the types are incompatible.
# Instead, use '7 <= what_time < 8' to check if the time is within the breakfast hour.

# i.e == needs to be exactly that. whereas below allows for a range.

    if 7 <= what_time < 8:
        print("breakfast time")
    elif 12 <= what_time < 13:
        print("lunch time")
    elif 18 <= what_time < 19:
        print("dinner time")

def convert(time):
    hour, min = time.split(":") # Split by the colon

    # Convert to float
    hour = float(hour)
    min = float(min) / 60

    # Creating time variable that will be returned
    time = hour + min

    return time

if __name__ == "__main__":
    main()
