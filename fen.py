#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖
# ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙
# . . . . . . . .
# . . . . . . . .
# . . . . . . . .
# . . . . . . . .
# ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟
# ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜

# Convert FEN to a Unicode chess board

import sys


def convert(fen):
    print(fen)

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
    convert(fen)

if __name__ == "__main__":
    main()
