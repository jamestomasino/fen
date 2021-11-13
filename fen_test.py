import unittest

from fen import (
    convert,
)

# Starting position
pos_start = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

# After 1. e4
pos_e4 = "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1"

class FenTest(unittest.TestCase):
    def test_start(self):
        self.assertEqual(convert(pos_start), "♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖\n\
♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙\n\
. . . . . . . .\n\
. . . . . . . .\n\
. . . . . . . .\n\
. . . . . . . .\n\
♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟\n\
♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜")


if __name__ == "__main__":
    unittest.main()
