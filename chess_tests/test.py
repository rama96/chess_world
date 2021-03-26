import chess
import pandas as pd
import numpy as np

def play_test_moves(board):

    board.push_uci("e2e4")
    board.push_uci("g8f6")
    board.push_uci("e4e5")
    board.push_uci("b8c6")
    board.push_uci("e5f6")
    board.push_uci("a7a6")
    board.push_uci("d2d4")
    board.push_uci("a6a5")
    board.push_uci("d4d5")
    board.push_uci("a5a4")
    board.push_uci("d5c6")
    return board

if __name__ == "__main__":
    board = chess.Board()
    play_test_moves(board)
    print(str(board))