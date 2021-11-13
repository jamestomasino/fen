# FEN to unicode board converter

Given an FEN, this program outputs the board in plain text using unicode chess characters.
```
$ ./fen.py r1bqkbnr/pp3p2/3p2p1/2p5/2BnP3/2N5/PPP3PP/R1BQ1RK1 w kq - 0 11

♖ . ♗ ♕ ♔ ♗ ♘ ♖
♙ ♙ . . . ♙ . .
. . . ♙ . . ♙ .
. . ♙ . . . . .
. . ♝ ♘ ♟ . . .
. . ♞ . . . . .
♟ ♟ ♟ . . . ♟ ♟
♜ . ♝ ♛ . ♜ ♚ .

$ ./fen.py "5r2/8/1R6/ppk3p1/2N3P1/P4b2/1K6/5B2 w - - 0 1"

. . . . . ♖ . .
. . . . . . . .
. ♜ . . . . . .
♙ ♙ ♔ . . . ♙ .
. . ♞ . . . ♟ .
♟ . . . . ♗ . .
. ♚ . . . . . .
. . . . . ♝ . .
```
