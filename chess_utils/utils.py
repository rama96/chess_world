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
    evaluation = white_eval - black_eval

    if board.turn:
        sign = 1
    else:
        sign = -1

    final_eval = evaluation * (sign)
    return final_eval


def search(board, depth ):
    """ Function to Search for the best possible moves in the position and returns the evaluation """
    
    ## Update recursion to see the number of calls made
    global count_recursion
    count_recursion += 1

    if depth == 0:
        return evaluate(board) , None 
    
    ## Fetch possiblle legal moves
    legal_moves = list(board.legal_moves)
    moves = order_moves(legal_moves , board)

    ## inital defn for the best evaluation
    max_eval = -1000
    best_move = None
    
    ## inital defn for the best evaluation
    for move in moves :
        
        # Play the move on analysis board 
        analysis_board = board.copy()
        analysis_board.push_uci(move.uci())
        
        # Evaluate the move 
        evaluation , calc_move = search(analysis_board , depth - 1 )
        
        # To implement min max  using sign change and correct evaluation metric
        evaluation = -(evaluation)
        
        # Saving the best moves to output in the current position
        if evaluation > max_eval :
           max_eval = evaluation
           best_move = move        
    
    return max_eval , best_move
        
def order_moves(moves , board):
    """Function to provide order to those moves to be analyzed for the alpha beta pruning which we plan to do in the future"""
    ordered_moves = moves
    return ordered_moves
    

if __name__ == "__main__":

    board = chess.Board()
    new_board = play_test_moves(board)
    print(new_board.turn)
    evaluation , best_move = search(new_board, depth = 3)
    print("Final Evaluation :" , evaluation , " With best move as :" , best_move)
    print(str(new_board))
    print("Number of moves Analyzed = " , count_recursion)

    