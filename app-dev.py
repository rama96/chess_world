from flask import Flask , redirect , url_for , request , render_template
app = Flask(__name__)
import pathlib
import json
import chess

board = chess.Board()

app = Flask(__name__,static_url_path='')


@app.route('/chess_board')
def chess_board():
    #print(board)
    #return render_template('chess_dev.html',fen=board.board_fen())
    global board
    print(board)
    return render_template('chess_dev.html',fen=board.board_fen())

@app.route('/')
def welcome_page():
    #print(board)
    #return render_template('chess_dev.html',fen=board.board_fen())
    print("Welcome Chess ")
    return render_template('index.html',fen=board.board_fen())

@app.route('/v2')
def welcome_page2():
    #print(board)
    #return render_template('chess_dev.html',fen=board.board_fen())
    print("Welcome Chess ")
    return render_template('index_2.html',fen=board.board_fen())

@app.route('/v3')
def welcome_page3():
    #print(board)
    #return render_template('chess_dev.html',fen=board.board_fen())
    print("Welcome Chess ")
    return render_template('index_3.html',fen=board.board_fen())

@app.route('/move', methods=['GET'])
def move():
    #print(board)
    #return render_template('chess_dev.html',fen=board.board_fen())
    global board
    print("Getting input from user")
    move_str = request.args.get('move',default = '')
    print("Input from user : " , move_str)
    move_uci = chess.Move.from_uci(move_str)
    #move_san = board.san(move_uci)
    
    print(move_uci)
    #print(move_san)
    print(board)
    if board.turn == True :
        print("White to move ")        
        board.push(move_uci)
    else :
        print("black to move")        
        board.push(move_uci)
    
    print(board)
    
    resp = {'fen':board.board_fen()}

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