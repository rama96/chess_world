from flask import Flask , redirect , url_for , requests
app = Flask(__name__)

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



## Flask - Http Methods 

# GET --  Sends data in encrypted form to server 
# HEAD - same as GET , but without response body 
# POST - Used to send HTML form of data to server 
# PUT - Replaces all current represenations of target resource witb uploaded content
# DELETE - Removes all current representations to target resource given by URL   


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name 

@app.route('/login',method = ['POST','GET'])
def success(name):
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success',name = user))
    else :
        user = request.args.get('nm')
        return redirect(url_for('success',name = user))


if __name__ == "__main__":
    app.run(debug = True)