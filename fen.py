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
validPieces = "♙♖♘♗♕♔♟♜♞♝♛♚."
validNum = "12345678"

def convert(fen):
    if len(fen) < 1:
        print("Improperly formatted FEN")
        raise SystemExit(1)
    output = ""
    lastChar = None
    for char in fen:
        if (char == " "):
            break
        if (char in validNum):
            if (lastChar != None) and (lastChar in validPieces):
                output += " "
            for x in range(int(char) - 1):
               output += ". "
            output += "."
            lastChar = "."
        else:
            try:
                newChar = pieces[char]
                # add spaces only between valid pieces
                if (lastChar != None) and (lastChar in validPieces) and (newChar in validPieces):
                    output += " "
                output += newChar
                lastChar = newChar
            except:
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
