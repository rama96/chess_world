import chess
import pandas as pd
import numpy as np
from chess_world.chess_utils.global_variables import sample_board
import traceback

class ChessPlayer:
    """ A class that has the chessboard stored and moves along with it """
    
    def __init__(self,board = sample_board , color = "White"):
        self.__initial_position = board.copy()
        self.__current_board = board.copy()
        self.__moves_played = []
        #self.color = color
        
    def get_board(self):
        """ Function that returns the curernt board status """
        return self.__current_board
    
    def set_board(self , board):
        """ Function to change the current board and import a new board. In the process of doiung so , it resets the moves stack """
        self.__current_board = board
        self.__moves_played = []
        
    def get_turn(self):
        """ Returns True/False based on which color to move """
        return self.__current_board.turn 
    
    def make_move(self , move):
        """ Function to make a move on the board """
        
        # Maybe Check for Invalid / Illegal Moves ??
        board = self.__current_board
        print("Printing the current board :: ")
        print(board)
        #self.__current_board = board.push_san(move)
        
        try :
            board.push_san(move)
            self.__current_board = board
        
        except Exception :
            traceback.print_exc()

    def reset_board(self):
        """ Resets the Board to the original Board Position """
        self.__current_board = self.__initial_position
        self.__moves_played = []
    
    def get_legal_moves(self):
        """ Resets the Board to the original Board Position """
        legal_moves_uci = list(self.__current_board.legal_moves) 
        legal_moves_san = []
        for move in legal_moves_uci:
            move_san = self.__current_board.san(move)
            legal_moves_san.append(move_san)
        return legal_moves_san

    def is_game_over(self):
        """ Function that returns boolean values for if game is over """
        # Work to be done
        legal_moves = self.get_legal_moves()
        if len(legal_moves) == 0 :
            print("Game Over No legal Moves Present ")
            return 0
        else:
            return 1
        