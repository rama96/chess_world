import chess 
import json 


count_recursion = 0

pieces_points = {
    chess.KING: 0,
    chess.PAWN: 1,
    chess.BISHOP: 3,
    chess.KNIGHT: 3,
    chess.ROOK: 5,
    chess.QUEEN: 9,
}

sample_board = chess.Board()