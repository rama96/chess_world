import pandas as pd
import numpy as np
import chess
from tests.test import play_test_moves
from chess_utils.global_variables import count_recursion , pieces_points


def CountMaterial(board, color):
    """ Function tht returns material count based on the values present in the global variables file"""
    if color == "White":
        i = True
    else:
        i = False

    total_points = 0

    for piece, points in pieces_points.items():
        total_points += len(list(board.pieces(piece, i))) * points
    return total_points


def evaluate(board):
    """ Function to evaluate a particular position based on just the difference in piece count """
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
    """ Function to Search for the best possible moves in the position """
    global count_recursion
    count_recursion = count_recursion + 1
    print(count_recursion)
    if depth == 0:
        return evaluate(board)
    
    legal_moves = list(board.legal_moves)
    moves = order_moves(legal_moves)

    max_eval = -1000
    for move in moves :
        analysis_board = board.copy()
        analysis_board.push_uci(move.uci())
        evaluation = -search(analysis_board , depth - 1 )
        max_eval = max(evaluation , max_eval)
    
    return max_eval
        
def order_moves(moves , board):
    """Function to provide order to those moves to be analyzed for the alpha beta pruning which we plan to do in the future"""
    ordered_moves = moves
    return ordered_moves
    

if __name__ == "__main__":

    board = chess.Board()
    new_board = play_test_moves(board)
    print(new_board.turn)
    print(search(new_board, depth = 4))
    print("Number of moves Analyzed = " , count_recursion)

    