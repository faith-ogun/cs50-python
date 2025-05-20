import random

def main():
    tries = 0
    num_questions = 0
    score = 0

    level = get_level()

    x = generate_integer(level) # now create a variable from the already generated function below.
    y = generate_integer(level) # x and y are shaded out only becuase they haven't been used yet. see no problems then keep going.

    while True:
        try:
            if num_questions >= 10:
                print(f"Score: {score}")
                break

            calc = x + y
            answer = int(input(f"{x} + {y} = "))

            if answer != calc:
                tries += 1
                print ("EEE")

                if tries >= 3:
                    print(f"{x} + {y} = {calc}")
                    num_questions += 1

                    x = generate_integer(level) # now create a variable from the already generated function below.
                    y = generate_integer(level) # x and y are shaded out only becuase they haven't been used yet. see no problems then keep going.

                    tries = 0

            if answer == calc:
                num_questions += 1
                score += 1
                tries = 0

                x = generate_integer(level) # now create a variable from the already generated function below.
                y = generate_integer(level) # x and y are shaded out only becuase they haven't been used yet. see no problems then keep going.
                continue

        except (ValueError):
            continue

        else: # At the end of the try block, just let it loop again. GOOD PRACTICE
            continue

def get_level():
    while True:
        try:
            level = int(input("Level: "))

            if 1 <= level <= 3: # This is for a range, understand logic, don't use "OR" here
                return level

        except (ValueError):
            continue

        else:
            continue

def generate_integer(level):
# level is in brackets from the previous function. so u won't really be creating a new variable, just using an already made one
    if level == 1:
        return random.randint(0, 9) # No need to create a new variable, just return directly

    elif level == 2:
        return random.randint(10, 99)

    elif level == 3:
        return random.randint(100, 999)

    else:
        raise ValueError("Invalid level.")

if __name__ == "__main__":
    main()
