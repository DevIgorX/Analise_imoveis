from flask import Flask
from routes import rotas
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.register_blueprint(rotas)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)


if __name__ == '__main__':
    app.run(debug=True)