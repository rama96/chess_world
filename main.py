from flask import Flask , redirect , url_for , request , render_template
app = Flask(__name__)
import pathlib

## Learning Flask Module 1 

@app.route('/admin/<name>')
def hello_admin(name):
    return 'You are the ADMIN SUCKKKA  %s'  % name

@app.route('/user/<name>')
def hello_user(name):
    if name != "rama" :
        return "You are a useless user %s"  %name
    else :
        # Rediects to admin  url with user argument
        return redirect(url_for('hello_admin' , name = 'krishna'))

@app.route('/')
def welcome_page():
    return "Welcome Ramamurthi Gopalakrishnan"

@app.route('/display_chess_board')
def chess_board():
    return render_template('chess.html')

@app.route('/chess_dev')
def chess_board_dev():
    return render_template('chess_dev.html')
    


## Flask - Http Methods 

# GET --  Sends data in encrypted form to server 
# HEAD - same as GET , but without response body 
# POST - Used to send HTML form of data to server 
# PUT - Replaces all current represenations of target resource witb uploaded content
# DELETE - Removes all current representations to target resource given by URL   

# Takes input from login.html and redirects the webpage to success(name)

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name 

@app.route('/login',methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success',name = user))
    else :
        user = request.args.get('nm')
        return redirect(url_for('success',name = user))


# uses Jinga2 template engine and takes input from hello.html for template purposes

@app.route('/hello/<user>')
def hello_name(user):
    return render_template('../flask_templates/hello.html' , name = user )

if __name__ == "__main__":
    app.run(debug = True)