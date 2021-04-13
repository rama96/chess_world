import chess
import pandas as pd
import numpy as np
from chess_world.chess_utils.global_variables import sample_board
import traceback

class ChessPlayer:
    """ A class that has the chessboard stored and moves along with it """
    
    def __init__(self,board = sample_board , color = "White"):
        self.__initial_position = board
        self.__current_board = board
        self.__moves_played = []
        #self.color = color
        
    def get_board(self):
        """ Function that returns the curernt board status """
        return self.__current_board
    
    def set_board(self , board):
        """ Function to change the current board and import a new board. In the process of doiung so , it resets the moves stack """
        self.__current_board = board
        self.__moves_played = []
        
    def is_turn(self):
        """ Returns True/False based on which color to move """
        return self.__current_board.turn == self.color
    
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

            # print("The Following Error Occured While Making the provided Move : " , str(Exception))
            # print(str(Exception.__class__)) 
            # print(str(Exception)) 
    
    def reset_board(self):
        """ Resets the Board to the original Board Position """
        self.__current_board = self.__initial_position
        self.__moves_played = []
    
    
    