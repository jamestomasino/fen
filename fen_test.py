# coding=utf-8
import pytest

from fen import (
    convert,
)

# Starting position
pos_start = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

# After 1. e4
pos_e4 = "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1"

# Invalid formatted FEN
pos_invalid = "rnbqkbnr/pppmpppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1"

def test_start():
    assert convert(pos_start) == "\
♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖\n\
♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙\n\
. . . . . . . .\n\
. . . . . . . .\n\
. . . . . . . .\n\
. . . . . . . .\n\
♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟\n\
♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜"

# def test_error():
#     with pytest.raises(Exception):
#         convert(pos_invalid)
