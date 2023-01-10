from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return 'hello flask with kashee!'
@app.route('/about')
def about_page():
    return 'This is a url shortener'