### Iteration 1

# greeting = input('Greeting: ').strip().lower()
#
# if "hello" in greeting:
# # This is to make sure that even if the phrase contains hello you get $0,
# #eg. "Hello, Newman", not just if it's hello alone
#     print("$0")
# elif greeting.startswith("h"):
#     print("$20")
# else:
#     print("$100")

####################

### Iteration 2

def main():
    greeting = input('Greeting: ') # taking the users input

    print(value(greeting)) # feeding it into value()

def value(greeting):
    greeting = greeting.strip().lower()  # Always normalise input

    # in general, it’s best to do input normalisation inside the non-main function,
    # especially if that function might be reused elsewhere (e.g. in tests, other scripts, or web apps).

    if "hello" in greeting:
    # This is to make sure that even if the phrase contains hello you get $0, eg. "Hello, Newman" not just if it's hello alone
        return 0

    elif greeting.startswith("h"):
        return 20

    else:
        return 100

if __name__ == "__main__":
    main()