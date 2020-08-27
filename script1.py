from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Homepage content goees here!"

@app.route('/about/')
def about():
    return "About content goes here"

if __name__ == "__main__":
    app.run(debug=True)