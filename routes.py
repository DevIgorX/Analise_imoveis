from flask import Blueprint, render_template, jsonify, request, redirect, url_for, flash
from models import Corretor, Imovel
from extensions import db


rotas = Blueprint('rotas',__name__)


@rotas.route('/')
def home():
  return render_template('home.html')

@rotas.route('/imoveis')
def index():
 imoveis = Imovel.query.order_by(Imovel.id)
 return render_template('index.html', lista_de_imoveis=imoveis)

@rotas.route('/cadastrar')
def cadastrar():
  return render_template('register.html')


# @rotas.route('/criar', methods=['POST',])
# def criar():
#   endereco = request.form['regiao']
#   preco = request.form['preco']
#   quartos = request.form['quartos']
#   terreno_total = request.form['area_total']
#   area_construida = request.form['area_construida']
#   valor_entrada = request.form['valor_entrada']
#   id_corretor = request.form['id_corretor']

#   novo_imovel = Imovel(endereco=endereco, preco=preco, quartos=quartos, terreno_total=terreno_total, area_construida=area_construida, valor_entrada=valor_entrada, id_corretor=id_corretor)
#   db.session.add(novo_imovel)
#   db.session.commit()
#   flash("Imovel cadastrado com sucesso!")
#   return redirect(url_for('rotas.index'))




