from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
@app.route('/index')
def index():
    return 'Hello Flask!'



@app.route("/meet")
def meet():
    return "Nice to meet you!"