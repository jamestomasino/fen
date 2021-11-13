#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Convert FEN to a Unicode chess board

import sys

# Dictionary for switcher-mapping
def p():
    return
def r():
    return
def n():
    return
def b():
    return
def q():
    return
def k():
    return
def P():
    return
def R():
    return
def N():
    return
def B():
    return
def Q():
    return
def K():
    return
def default():
    return ""

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
    "8": ". . . . . . . . "
}

def convert(fen):
    output = ""
    for char in fen:
        if (char == " "):
            break
        if (char == "/"):
            output += "\n"
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
