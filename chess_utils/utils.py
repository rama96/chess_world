import pandas as pd 
import numpy as np
import chess

#len(board.pieces(chess.ROOK, True))

pieces_points = {
                chess.KING : 0 
                , chess.PAWN : 1 
                , chess.BISHOP : 3
                ,  chess.KNIGHT : 3 
                , chess.ROOK : 5 
                , chess.QUEEN : 9 
                }

def CountMaterial(board , color):
    
    if color == "White":
        i = True
    else :
        i = False

    total_points = 0 

    for piece, points in pieces_points.items():
        total_points += (len(list(board.pieces(piece, i))) * points)
    return total_points


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

def evalutate(board):
    pass


if __name__ == "__main__":
    
    board = chess.Board()
    new_board = play_test_moves(board)
    print(CountMaterial(new_board , "White"))
    print(CountMaterial(new_board , "Black"))



