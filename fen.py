#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Convert FEN to a Unicode chess board

import sys

pieces = {
    "p": "♙ ",
    "r": "♖ ",
    "n": "♘ ",
    "b": "♗ ",
    "q": "♕ ",
    "k": "♔ ",
    "P": "♟ ",
    "R": "♜ ",
    "N": "♞ ",
    "B": "♝ ",
    "Q": "♛ ",
    "K": "♚ ",
    "1": ". ",
    "2": ". . ",
    "3": ". . . ",
    "4": ". . . . ",
    "5": ". . . . . ",
    "6": ". . . . . . ",
    "7": ". . . . . . . ",
    "8": ". . . . . . . . ",
    "/": "\n"
}

def convert(fen):
    output = ""
    for char in fen:
        if (char == " "):
            break
        else:
            output += pieces[char]
    return output

def main():
    # Read standard in as one big string
    fen = ""
    if len(sys.argv) > 2:
        params = sys.argv[1::]
        fen = " ".join(params)
    elif len(sys.argv) == 2:
        fen = sys.argv[1]
    else:
        print("Requires FEN as parameter")
        sys.exit()
    print(convert(fen))

if __name__ == "__main__":
    main()
