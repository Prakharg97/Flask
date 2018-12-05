from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)
@app.route('/')
def upload_file():
   return render_template('login.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['Name'] != 'admin' or request.form['Password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            error='Successful'
    return render_template('dis.html', error=error)
if __name__ == '__main__':
   app.run(debug = True)

