from flask import Blueprint, render_template, jsonify, request, redirect, url_for, flash
from models import Corretores, Imoveis
from extensions import db
from services import (create_corretor, create_imovel, edit_imovel)


rotas = Blueprint('rotas',__name__)


@rotas.route('/')
def home():
  return render_template('home.html')

@rotas.route('/imoveis')
def index():
 imoveis = Imoveis.query.order_by(Imoveis.id)
 return render_template('index.html', lista_de_imoveis=imoveis)

@rotas.route('/cadastrar_imovel_template')
def cadastrar():
  corretores = Corretores.query.all()
  return render_template('create_imovel.html', corretores=corretores)

@rotas.route('/cadastrar_corretor_template')
def cadastrar_imo():
   return render_template('create_corretor.html')

@rotas.route('/cadastrar_corretor', methods=['POST',])
def cadastrar_corretor():
  return create_corretor(request)


@rotas.route('/criar', methods=['POST',])
def criar():
  return create_imovel(request)
  

@rotas.route('/editar/<int:id>')
def editar(id):
  imovel = Imoveis.query.filter_by(id=id).first()
  corretores = Corretores.query.all()
  return render_template('edit_imovel.html',imovel=imovel,corretores=corretores)

@rotas.route('/atualizar', methods=['POST'])
def atualizar(): 
  return edit_imovel(request)

@rotas.route('/deletar/<int:id>')
def deletar(id):
 
 Imoveis.query.filter_by(id=id).delete()
 db.session.commit()

 flash( 'Imovel Deletado!')

 return redirect(url_for('rotas.index'))




 




