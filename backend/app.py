from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

@app.route('/')
def home():
    return "Hello, Flask!, Welcome to Jonai Template!"

if __name__ == '__main__':
    app.run(debug=True)
