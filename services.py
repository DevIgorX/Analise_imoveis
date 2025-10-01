from flask import  redirect, url_for, flash
from models import Corretores, Imoveis
from extensions import db

def create_corretor(request):
  nome_corretor = request.form['nome']
  contato = request.form['contato']

  corretor = Corretores.query.filter_by(nome=nome_corretor).first()

  if corretor:
    flash(f'O corretor {corretor.nome} já existe no banco de dados.')  
    return redirect(url_for('rotas.cadastrar_imo'))
  else:
   novo_corretor = Corretores(nome=nome_corretor, contato=contato) 
   db.session.add(novo_corretor)
   db.session.commit()
   flash("Corretor Cadastrado com Sucesso")
   return redirect(url_for('rotas.index'))
  
def create_imovel(request):
  
  bairro = request.form['bairro']
  cidade = request.form['cidade']
  preco = request.form['preco']
  quartos = request.form['quartos']
  area_total = request.form['area_total']
  area_construida = request.form['area_construida']
  area_gourmet = request.form['area_gourmet']
  suite = request.form['suite']
  valor_entrada = request.form['valor_entrada']
  link_anuncio = request.form['link_anuncio']
  nome_corretor = request.form['nome_corretor']

  corretor = Corretores.query.filter_by(nome=nome_corretor).first() 

  if corretor:
   novo_imovel = Imoveis(bairro=bairro, cidade=cidade, preco=preco, quartos=quartos, area_total=area_total, area_construida=area_construida,area_gourmet= area_gourmet, suite=suite, valor_entrada=valor_entrada, link_anuncio=link_anuncio , id_corretor=corretor.id)
   db.session.add(novo_imovel)
   db.session.commit()
   flash("Imovel cadastrado com sucesso!")
   return redirect(url_for('rotas.index'))
  else: 
   flash("Corretor não existe no banco de dados")
   return redirect(url_for('rotas.cadastrar'))
  
def edit_imovel(request):
 
  imovel = Imoveis.query.filter_by(id=request.form['id']).first()
  imovel.bairro = request.form['bairro']  # type: ignore
  imovel.cidade = request.form['cidade'] # type: ignore
  imovel.preco  = request.form['preco'] # type: ignore
  imovel.quartos = request.form['quartos'] # type: ignore
  imovel.area_total = request.form['area_total']# type: ignore
  imovel.area_construida = request.form['area_construida']# type: ignore
  imovel.area_gourmet = request.form['area_gourmet']# type: ignore
  imovel.suite = request.form['suite']# type: ignore
  imovel.valor_entrada = request.form['valor_entrada']# type: ignore
  imovel.link_anuncio = request.form['link_anuncio']# type: ignore
  imovel.nome_corretor = request.form['nome_corretor']# type: ignore

  db.session.add(imovel)
  db.session.commit()

  return redirect(url_for('rotas.index'))

def deletar_imovel(id):
 
 Imoveis.query.filter_by(id=id).delete()
 db.session.commit()

 flash( 'Imovel Deletado!')

 return redirect(url_for('rotas.index'))