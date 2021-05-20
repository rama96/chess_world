from flask import Flask , redirect , url_for , request , render_template
app = Flask(__name__)
import pathlib
import json
import chess

board = chess.Board()
board.push_san("e4")

app = Flask(__name__)

@app.route('/chess_board')
def chess_board():
    #print(board)
    #return render_template('chess_dev.html',fen=board.board_fen())
    global board
    print(board)
    return render_template('index.html')

@app.route('/')
def welcome_page():
    #print(board)
    #return render_template('chess_dev.html',fen=board.board_fen())
    return "HEllo"

@app.route('/move', methods=['GET'])
def move():
    #print(board)
    #return render_template('chess_dev.html',fen=board.board_fen())
    global board
    move_san = request.args.get('move',default = '')
    print(board)
    if board.turn == True :
        board = board.make_move(move_san)
    else :
        print("Make a move -- ")        
        move = input()
        board = board.make_move(move_san)
    resp = {'fen':board.FEN }

    response = app.response_class(
        response = json.dumps(resp),
        status = 200 ,
        mimetype = 'application/json'
    )
    return response

@app.route('/print_board')
def print_board():
    #print(board)
    #return render_template('chess_dev.html',fen=board.board_fen())
    global board
    print(board)
    return "board"

@app.route('/get_current_position')
def get_current_pos():
    return "Hello"


if __name__ == "__main__":
    app.run(debug = True)