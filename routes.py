from flask import Blueprint, render_template, jsonify, request, redirect, url_for, flash
from models import Corretores, Imoveis
from extensions import db


rotas = Blueprint('rotas',__name__)


@rotas.route('/')
def home():
  return render_template('home.html')

@rotas.route('/imoveis')
def index():
 imoveis = Imoveis.query.order_by(Imoveis.id)
 return render_template('index.html', lista_de_imoveis=imoveis)

@rotas.route('/cadastrar')
def cadastrar():
  return render_template('register.html')




@rotas.route('/criar', methods=['POST',])
def criar():
  regiao = request.form['regiao']
  preco = request.form['preco']
  quartos = request.form['quartos']
  area_total = request.form['area_total']
  area_construida = request.form['area_construida']
  area_gourmet = request.form['area_gourmet']
  valor_entrada = request.form['valor_entrada']
  link_anuncio = request.form['link_anuncio']
  id_corretor = request.form['id_corretor']

  novo_imovel = Imoveis(regiao=regiao, preco=preco, quartos=quartos, area_total=area_total, area_construida=area_construida,area_gourmet= area_gourmet, valor_entrada=valor_entrada, link_anuncio=link_anuncio , id_corretor=id_corretor)
  db.session.add(novo_imovel)
  db.session.commit()
  flash("Imovel cadastrado com sucesso!")
  return redirect(url_for('rotas.index'))



