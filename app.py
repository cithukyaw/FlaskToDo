from flask import Flask
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy

# My App
app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True)
