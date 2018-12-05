from flask import Flask, render_template
from socket import gethostname
app = Flask(__name__)
#sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

@app.route('/hello/<int:score>')
def hello_name(score):
   return render_template('hello.html', marks = score)

if __name__ == '__main__':
   #db.create_all()
   #if 'liveconsole' not in gethostname():
      app.run(debug = True)
