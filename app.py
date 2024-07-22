from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/random')
def random_number():
    number = random.randint(1, 100)
    return f'Random number: {number}'

if __name__ == '__main__':
    app.run(debug=True)
