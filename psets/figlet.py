import sys
import pyfiglet
import random

# Get all available fonts
available_fonts = [
    '3-d', '3x5', '5lineoblique', 'acrobatic', 'alligator', 'alligator2', 'alphabet', 'avatar', 'banner',
    'banner3-D', 'banner3', 'banner4', 'barbwire', 'basic', 'bell', 'big', 'bigchief', 'binary', 'block',
    'bubble', 'bulbhead', 'calgphy2', 'caligraphy', 'catwalk', 'chunky', 'coinstak', 'colossal', 'computer',
    'contessa', 'contrast', 'cosmic', 'cosmike', 'cricket', 'cursive', 'cyberlarge', 'cybermedium',
    'cybersmall', 'diamond', 'digital', 'doh', 'doom', 'dotmatrix', 'drpepper', 'eftichess', 'eftifont',
    'eftipiti', 'eftirobot', 'eftitalic', 'eftiwall', 'eftiwater', 'epic', 'fender', 'fourtops', 'fuzzy',
    'goofy', 'gothic', 'graffiti', 'hollywood', 'invita', 'isometric1', 'isometric2', 'isometric3',
    'isometric4', 'italic', 'ivrit', 'jazmine', 'jerusalem', 'katakana', 'kban', 'larry3d', 'lcd', 'lean',
    'letters', 'linux', 'lockergnome', 'madrid', 'marquee', 'maxfour', 'mike', 'mini', 'mirror', 'mnemonic',
    'morse', 'moscow', 'nancyj-fancy', 'nancyj-underlined', 'nancyj', 'nipples', 'ntgreek', 'o8', 'ogre',
    'pawp', 'peaks', 'pebbles', 'pepper', 'poison', 'puffy', 'pyramid', 'rectangles', 'relief', 'relief2',
    'rev', 'roman', 'rot13', 'rounded', 'rowancap', 'rozzo', 'runic', 'runyc', 'sblood', 'script', 'serifcap',
    'shadow', 'short', 'slant', 'slide', 'slscript', 'small', 'smisome1', 'smkeyboard', 'smscript',
    'smshadow', 'smslant', 'smtengwar', 'speed', 'stampatello', 'standard', 'starwars', 'stellar', 'stop',
    'straight', 'tanja', 'tengwar', 'term', 'thick', 'thin', 'threepoint', 'ticks', 'ticksslant',
    'tinker-toy', 'tombstone', 'trek', 'tsalagi', 'twopoint', 'univers', 'usaflag', 'wavy', 'weird'
]

random_font = random.choice(available_fonts)

# sys.exit cases for incorrect number of arguments
if len(sys.argv) == 2 or len(sys.argv) > 3:
    sys.exit("Invalid usage") # No need for extra print line, just keep text in sys.exit()

# sys.argv == 3 handling:

if len(sys.argv) == 3:
    flag = sys.argv[1]
    font = sys.argv[2]

    if flag != "--font" and flag != "-f": # make sure to use the correct conditional (and/or)
        sys.exit("Invalid usage")

    if font not in available_fonts:
        sys.exit("Invalid usage")

    phrase = input("Input: ") # input AFTER checks
    print(f"Output: {pyfiglet.figlet_format(phrase, font=font)}")

# sys.argv == 1 handling:
if len(sys.argv) == 1:
    phrase = input("Input: ")
    print(f"Output: {pyfiglet.figlet_format(phrase, font=random_font)}")
