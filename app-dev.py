from flask import Flask , redirect , url_for , request , render_template
app = Flask(__name__)
import pathlib


app = Flask(__name__)


@app.route('/chess_board')
def chess_board():
    return render_template('chess_dev.html')


if __name__ == "__main__":
    app.run(debug = True)