from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)
mail=Mail(app)



@app.route('/')
def student():
   return render_template('email.html')

@app.route('/email',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      fr = request.form['from']
      password=request.form['password']
      to=request.form['to']
      sub=request.form['subject']
      body=request.form['body']
      print(fr,password,to,sub,body)
      app.config['MAIL_SERVER']='smtp.gmail.com'
      app.config['MAIL_PORT'] = 465
      app.config['MAIL_USERNAME'] = fr
      app.config['MAIL_PASSWORD'] = password
      app.config['MAIL_USE_TLS'] = False
      app.config['MAIL_USE_SSL'] = True
      mail = Mail(app)
      msg = Message(sub, sender = fr, recipients = [to])
      msg.body = body
      mail.send(msg)
      return "Your mail has been sent"

if __name__ == '__main__':
   app.run(debug = True)
