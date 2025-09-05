from flask import Blueprint, render_template, jsonify, request, redirect, url_for, flash
from services import imoveis, Imoveis


rotas = Blueprint('rotas',__name__)


@rotas.route('/')
def home():
  return render_template('home.html')

@rotas.route('/imoveis')
def index():
 return render_template('index.html', lista_de_imoveis=imoveis)

@rotas.route('/cadastrar')
def cadastrar():
  return render_template('register.html')


@rotas.route('/criar', methods=['POST',])
def criar():
  endereco = request.form['endereco']
  preco = request.form['preco']
  quartos = request.form['quartos']
  terreno_total = request.form['terreno_total']
  link = request.form['link']
  corretor = request.form['corretor']
  telefone_corretor = request.form['telefone_corretor']

  novo_imovel = Imoveis(endereco, preco, quartos , terreno_total , link,  corretor, telefone_corretor )
  imoveis.append(novo_imovel)
  flash("Imovel cadastrado com sucesso!")
  return redirect(url_for('rotas.index'))



# @rotas.route('/login')
# def login():

