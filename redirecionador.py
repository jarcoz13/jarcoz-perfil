from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/alejandro')
def hello_alejandro():
   return 'Hello alejandro'

@app.route('/miguel')
def hello_miguel():
   return 'Hello miguel'

@app.route('/sebastian')
def hello_sebastian():
   return 'Hello sebastian'
   
@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))

if __name__ == '__main__':
   app.run(debug = True)
