from flask import Flask, render_template
from routes import rotas
# Cria a nossa aplicação
app = Flask(__name__)

app.register_blueprint(rotas)

app.secret_key = 'alura'

# Adição para rodar o app diretamente
if __name__ == '__main__':
    app.run(debug=True)