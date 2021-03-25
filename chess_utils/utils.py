import pandas as pd
import numpy as np
import chess
from tests.test import play_test_moves


count_recursion = 0

pieces_points = {
    chess.KING: 0,
    chess.PAWN: 1,
    chess.BISHOP: 3,
    chess.KNIGHT: 3,
    chess.ROOK: 5,
    chess.QUEEN: 9,
}


def CountMaterial(board, color):

    if color == "White":
        i = True
    else:
        i = False

    total_points = 0

    for piece, points in pieces_points.items():
        total_points += len(list(board.pieces(piece, i))) * points
    return total_points


def evaluate(board):

    white_eval = CountMaterial(board, "White")
    black_eval = CountMaterial(board, "Black")
    eval = white_eval - black_eval

    if board.turn:
        sign = 1
    else:
        sign = -1

    final_eval = eval * (sign)
    return final_eval


def search(board, depth ):
 
    global count_recursion
    count_recursion = count_recursion + 1
    
    if depth == 0:
        return evaluate(board)
    
    legal_moves = list(board.legal_moves)
    
    max_eval = -1000
    for move in legal_moves :
        analysis_board = board.copy()
        analysis_board.push_uci(move.uci())
        evaluation = -search(analysis_board , depth - 1 )
        max_eval = max(evaluation , max_eval)
    
    return max_eval
        


    
    print(legal_moves)


if __name__ == "__main__":

    print(count_recursion)
    board = chess.Board()
    new_board = play_test_moves(board)
    print(CountMaterial(new_board, "White"))
    print(CountMaterial(new_board, "Black"))
    print(evaluate(board))
    print(new_board.turn)
    print(search(new_board, depth = 4))
    print("Number of moves Analyzed = " , count_recursion)
    