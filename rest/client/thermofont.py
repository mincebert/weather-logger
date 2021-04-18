# thermo.py
#
# Font for thermometer.


# general dimensions of the characters (but width can vary0

width = 3
height = 5


# chars = [[]]
#
# These are the character definitions - these not in the format
# required for the scrollphathd fonts (see below) but are in a simpler
# format to view/edit and are converted by the function below.

_chars1 = {
    " ": [
        "   ",
        "   ",
        "   ",
        "   ",
        "   ",
    ],

    "0": [
        " # ",
        "# #",
        "# #",
        "# #",
        " # ",
    ],

    "1": [
        "## ",
        " # ",
        " # ",
        " # ",
        "###",
    ],

    "2": [
        "## ",
        "  #",
        " # ",
        "#  ",
        "###",
    ],

    "3": [
        "## ",
        "  #",
        " # ",
        "  #",
        "## ",
    ],

    "4": [
        "# #",
        "# #",
        "###",
        "  #",
        "  #",
    ],

    "5": [
        "###",
        "#  ",
        "## ",
        "  #",
        "## ",
    ],

    "6": [
        " # ",
        "#  ",
        "## ",
        "# #",
        " # ",
    ],

    "7": [
        "###",
        "  #",
        " # ",
        " # ",
        " # ",
    ],

    "8": [
        " # ",
        "# #",
        " # ",
        "# #",
        " # ",
    ],

    "9": [
        " # ",
        "# #",
        " ##",
        "  #",
        " # ",
    ],

    ".": [
        " ",
        " ",
        " ",
        " ",
        "#",
    ],

    "'": [
        " # ",
        "# #",
        " # ",
        "   ",
        "   ",
    ],

    "-": [
        "   ",
        "   ",
        "###",
        "   ",
        "   ",
    ],

    "%": [
        "# #",
        "  #",
        " # ",
        "#  ",
        "# #",
    ],
}


_chars = {
    " ": [
        "   ",
        "   ",
        "   ",
        "   ",
        "   ",
    ],

    "0": [
        "###",
        "# #",
        "# #",
        "# #",
        "###",
    ],

    "1": [
        "## ",
        " # ",
        " # ",
        " # ",
        "###",
    ],

    "2": [
        "###",
        "  #",
        "###",
        "#  ",
        "###",
    ],

    "3": [
        "###",
        "  #",
        "###",
        "  #",
        "###",
    ],

    "4": [
        "# #",
        "# #",
        "###",
        "  #",
        "  #",
    ],

    "5": [
        "###",
        "#  ",
        "###",
        "  #",
        "###",
    ],

    "6": [
        "###",
        "#  ",
        "###",
        "# #",
        "###",
    ],

    "7": [
        "###",
        "  #",
        "  #",
        "  #",
        "  #",
    ],

    "8": [
        "###",
        "# #",
        "###",
        "# #",
        "###",
    ],

    "9": [
        "###",
        "# #",
        "###",
        "  #",
        "###",
    ],

    ".": [
        " ",
        " ",
        " ",
        " ",
        "#",
    ],

    "'": [
        "###",
        "# #",
        "###",
        "   ",
        "   ",
    ],

    "-": [
        "   ",
        "   ",
        "###",
        "   ",
        "   ",
    ],

    "%": [
        "# #",
        "  #",
        " # ",
        "#  ",
        "# #",
    ],
}


# build the font data required for the scrollphathd module: these must
# be stored in a dictionary called 'data', keyed on the character code
# and containing a list of rows, each row a list of brightness values,
# expressed as a byte from 0x00 (off) to 0xff (on)
#
# we transform the above '_chars' dictionary into this format here


data = {}
for char in _chars:
    data[char] = [
        [ 0x00 if col == " " else 0xff for col in row ]
        for row in _chars[char] ]