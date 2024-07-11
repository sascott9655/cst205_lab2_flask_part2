from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)


dictionary = {
    'people': ['Eddie', 'Brendan'],
    'food': ['eggs', 'red meat']
} 


@app.route('/')
def home():
   return render_template('index.html', dictionary=dictionary)
