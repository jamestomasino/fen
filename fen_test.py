# coding=utf-8
import pytest

from fen import (
    convert,
)

# Starting position
pos_start = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
start_output = "\
♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖\n\
♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙\n\
. . . . . . . .\n\
. . . . . . . .\n\
. . . . . . . .\n\
. . . . . . . .\n\
♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟\n\
♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜"

# After 1. e4
pos_e4 = "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1"
e4_output = "\
♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖\n\
♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙\n\
. . . . . . . .\n\
. . . . . . . .\n\
. . . . ♟ . . .\n\
. . . . . . . .\n\
♟ ♟ ♟ ♟ . ♟ ♟ ♟\n\
♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜"

# Invalid formatted FEN
pos_invalid = "rnbqkbnr/pppmpppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1"

# Empty data
pos_empty = ""

def test_start():
    assert convert(pos_start) == start_output
    assert convert(pos_e4) == e4_output

def test_error():
    with pytest.raises(SystemExit):
        convert(pos_invalid)
    with pytest.raises(SystemExit):
        convert(pos_empty)
