from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


# does not give 404 error on some mistakes.
if __name__ == '__main__':
    # app.run()
    app.run(debug=True)


