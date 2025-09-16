from flask import Flask
from routes import rotas
from extensions import db

app = Flask(__name__)


app.config.from_pyfile('config.py')
db.init_app(app)
app.register_blueprint(rotas)

if __name__ == '__main__':
    app.run(debug=True)