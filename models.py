from extensions import db

class Corretores(db.Model):
    __tablename__ = 'Corretores'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String,nullable=False)
    contato = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Corretor {self.nome}>'


class Imoveis(db.Model):
    __tablename__ = 'Imoveis'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    bairro = db.Column(db.String, nullable=False)   
    cidade = db.Column(db.String, nullable=False) 
    estado = db.Column(db.String, nullable=False, default='Go')   
    preco = db.Column(db.Integer, nullable=False)
    quartos = db.Column(db.Integer, nullable=False)
    area_total = db.Column(db.String)
    area_construida = db.Column(db.String)
    area_gourmet = db.Column(db.String)
    suite = db.Column(db.String)
    valor_entrada = db.Column(db.Integer)
    link_anuncio = db.Column(db.String, nullable=False)
    id_corretor = db.Column(db.Integer, db.ForeignKey('Corretores.id'), nullable=False)
    corretor = db.relationship('Corretores', backref='Imoveis')
    
    
    def __repr__(self):
        return f'<Imovel {self.bairro}, R${self.preco}>'