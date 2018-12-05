import random
from flask import Flask, render_template, request
from flask import Markup
app = Flask(__name__)
@app.route('/')
def index():
    x=[]
    y=[] 
    #print("Hello")
    for i in range (10):
      x.append(random.randint(1, 10))
      #y.append(chr(random.randint(ord('a'),ord('z'))))
      y.append(random.randint(1, 10))
    return render_template('new.html', values=x,labels=y)
if __name__ == '__main__':
   app.run(debug = True)
#print(x,y)
   
    
    #my_randoms.append(random.randrange(1,101,1)) 
#chr(random.randint(ord(a), ord(b))
