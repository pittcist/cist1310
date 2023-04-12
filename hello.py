from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    # return 'Hello <b>World</b>!'
    return render_template('login.htm')

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello {0}!'.format(name) 

@app.route('/blog/<int:postID>')
def show_post(postID):
    return 'Post number {0}'.format(postID)

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['um']
        pswd = request.form['pw']
        if user == 'test':
            return render_template('welcome.htm', name=user)
        else:
            return render_template('rejection.htm', name=user)

if __name__ == "__main__":
    app.run(debug=True)
