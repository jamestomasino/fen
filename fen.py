#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Convert FEN to a Unicode chess board

import sys

pieces = {
    "p": "♙",
    "r": "♖",
    "n": "♘",
    "b": "♗",
    "q": "♕",
    "k": "♔",
    "P": "♟",
    "R": "♜",
    "N": "♞",
    "B": "♝",
    "Q": "♛",
    "K": "♚",
    "/": "\n"
}
valid_s = "♙♖♘♗♕♔♟♜♞♝♛♚."
valid_n = "12345678"

def convert(fen):
    # if empty data, invalid
    if len(fen) < 1:
        print("Improperly formatted FEN")
        raise SystemExit(1)

    output = ""
    prev = None

    for char in fen:
        # break in FEN ends position setup
        if (char == " "):
            break
        # handle n spaces
        if (char in valid_n):
            if (prev != None) and (prev in valid_s):
                output += " "
            for x in range(int(char) - 1):
               output += ". "
            output += "."
            prev = "."
        # handle all valid character pieces
        else:
            try:
                newChar = pieces[char]
                # add spaces between piece positions (not beginning or EOL)
                if (prev != None) and (prev in valid_s) and (newChar in valid_s):
                    output += " "
                output += newChar
                prev = newChar
            except:
                # if we encounter an unhandled character the FEN must be bad
                print("Improperly formatted FEN")
                raise SystemExit(1)
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
        raise SystemExit(1)
    print(convert(fen))

if __name__ == "__main__":
    main()
