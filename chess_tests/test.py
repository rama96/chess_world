import chess
import pandas as pd
import numpy as np
from chess_world.chess_utils.chess_players import ChessPlayer
import time 

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

def play_test_moves_san(board):

    board.push_san("e4")
    board.push_san("e5")
    board.push_san("Nf3")
    board.push_san("Nc6")
    board.push_san("Bc4")
    board.push_san("Bc5")
    board.push_san("c3")
    board.push_san("Nf6")
    board.push_san("d3")
    board.push_san("d6")
    board.push_san("h3")
    return board



if __name__ == "__main__":
    
    print("*"*25,"Test 1 : Making Moves from a random position" ,"*"*25)
    board = chess.Board()
    play_test_moves_san(board)
    Board1 = ChessPlayer(board)
    Board1.make_move("h6")
    print("Prinitng New Board -- ")
    print(Board1.get_board())
    print("*"*50)
    
    
    print("*"*25,"Test 2 : Without giving any args" ,"*"*25)
    Board2 = ChessPlayer()
    print(Board2.get_board())
    Board2.make_move("e4")
    Board2.make_move("e5")
    print(Board2.get_board())
    Board2.reset_board()
    print(Board2.get_board())
    
    print("*"*25,"Test 3 : Without giving any args" ,"*"*25)
    Board2 = ChessPlayer()
    print(Board2.get_board())
    Board2.make_move("e4")
    Board2.make_move("e5")
    Board2.make_move("Nf3")
    print(Board2.get_turn())
    
    print("*"*25,"Test 4 : Legal Moves " ,"*"*25)
    print(Board2.legal_moves())