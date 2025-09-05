from flask import Blueprint, render_template, jsonify
from services import imoveis


rotas = Blueprint('rotas',__name__)


@rotas.route('/')
def index():
 return render_template('index.html', lista_de_imoveis=imoveis)


@rotas.route('/cadastrar')
def cadastrar():
  

  return jsonify({'mensagem': 'alguma coisa'})



