### Iteration 1

# input = input("Input: ")
#
# word = ""
#
# for char in input:
#     if char.lower() in ["a", "e", "i", "o", "u"]:
#         word += char.replace(char, "") # must use replace as .remove() is a list method.
#     else:
#         word += char
#
# print(f"Output: {word}")

####################

### Iteration 2

def main():
    output = shorten(input("Input: "))
    print(f"Output: {output}")

def shorten(word): # word is the input from main, result is returned.
    result = ""

    for char in word:
        if not char.lower() in ["a", "e", "i", "o", "u"]:
            result += char

            # else: result += "", isn't needed, as removing else, i.e doing nothing), is the same thing.
            # Only use else when you need an action for the opposite case.
            # also don't need to use replace.

    return result

if __name__ == "__main__":
    main()
