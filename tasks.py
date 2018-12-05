from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_name(user):
   return render_template('ta.html')

if __name__ == '__main__':
   app.run(debug = True)
