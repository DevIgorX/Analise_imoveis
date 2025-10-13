from flask import Blueprint, render_template,request
from models import Corretores, Imoveis
from services import (create_corretor, create_imovel, edit_imovel, deletar_imovel,excluir_correto, edit_corretor)
from sqlalchemy import func
from extensions import db


rotas = Blueprint('rotas',__name__)


@rotas.route('/')
def home():
  qtd_imoveis = Imoveis.query.count()
  qtd_corretores = Corretores.query.count()
  return render_template('home.html',qtd_imoveis = qtd_imoveis, qtd_corretores = qtd_corretores)

@rotas.route('/imoveis')
def index():
 imoveis = Imoveis.query.order_by(Imoveis.id)
 return render_template('index.html', lista_de_imoveis=imoveis)

@rotas.route('/corretores')
def lista_corretores():
 corretores = Corretores.query.order_by(Corretores.id)
 return render_template('list_corretores.html', lista_de_corretores=corretores)

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
 return deletar_imovel(id)


@rotas.route('/editar_corretor/<int:id>')
def editar_corretor(id):
  corretor = Corretores.query.filter_by(id=id).first()
  return render_template('edit_corretor.html', corretor=corretor)

@rotas.route('/atualizar_corretor', methods=['POST'])
def atualizar_corretor():
  return edit_corretor(request)

@rotas.route('/deletar_corretor/<int:id>')
def deletar_corretor(id):
 return excluir_correto(id)


@rotas.route('/analise', methods=['GET', 'POST'])
def analise():
    cidades = db.session.query(Imoveis.cidade).distinct().all()
    corretores = Corretores.query.all()

    cidade_selecionada = request.form.get('cidade')
    corretor_selecionado = request.form.get('corretor')

    query = Imoveis.query

    if cidade_selecionada:
        query = query.filter(Imoveis.cidade == cidade_selecionada)

    if corretor_selecionado:
        query = query.filter(Imoveis.id_corretor == corretor_selecionado)

    imoveis_filtrados = query.all()

    # Análises
    media_preco_geral = db.session.query(func.avg(Imoveis.preco)).scalar()
    media_preco_cidade = None
    if cidade_selecionada:
        media_preco_cidade = db.session.query(func.avg(Imoveis.preco)).filter(Imoveis.cidade == cidade_selecionada).scalar()
    
    imoveis_por_corretor = db.session.query(Corretores.nome, func.count(Imoveis.id)).join(Imoveis).group_by(Corretores.nome).all()


    return render_template('analysis.html',
                           cidades=[c[0] for c in cidades],
                           corretores=corretores,
                           imoveis_filtrados=imoveis_filtrados,
                           cidade_selecionada=cidade_selecionada,
                           corretor_selecionado=corretor_selecionado,
                           media_preco_geral=media_preco_geral,
                           media_preco_cidade=media_preco_cidade,
                           imoveis_por_corretor=imoveis_por_corretor)

  





 




