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
  return render_template('create_imovel.html')

@rotas.route('/cadastrar_corretor')
def cadastrar_imo():
   return render_template('create_corretor.html')

@rotas.route('/cadastrar_corretor', methods=['POST',])
def cadastrar_corretor():

  nome_corretor = request.form['nome']
  contato = request.form['contato']

  corretor = Corretores.query.filter_by(nome=nome_corretor).first()

  if corretor:
    flash(corretor.nome + 'já existe no banco de dados')  
    return redirect('/')
  else:
   novo_corretor = Corretores(nome=nome_corretor, contato=contato)
   db.session.add(novo_corretor)
   db.session.commit()
   flash("Corretor Cadastrado com Sucesso")
   return redirect(url_for('rotas.cadastrar'))
  

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
  nome_corretor = request.form['nome_corretor']

  corretor = Corretores.query.filter_by(nome=nome_corretor).first() 

  if corretor:
   novo_imovel = Imoveis(regiao=regiao, preco=preco, quartos=quartos, area_total=area_total, area_construida=area_construida,area_gourmet= area_gourmet, valor_entrada=valor_entrada, link_anuncio=link_anuncio , id_corretor=corretor)
   db.session.add(novo_imovel)
   db.session.commit()
   flash("Imovel cadastrado com sucesso!")
  else: 
   flash("Corretor já existe no banco de dados")
   return redirect(url_for('rotas.index'))



