import pandas as pd 
import numpy as np
import chess
from tests.test import play_test_moves 
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



def evalutate(board):
    pass


if __name__ == "__main__":
    
    board = chess.Board()
    new_board = play_test_moves(board)
    print(CountMaterial(new_board , "White"))
    print(CountMaterial(new_board , "Black"))



