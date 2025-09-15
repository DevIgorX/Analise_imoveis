from app import db

class Corretor(db.Model):
    __tablename__ = 'corretores'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String,nullable=False)
    contato = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Corretor {self.nome}>'


class Imovel(db.Model):
    __tablename__ ='imoveis'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    regiao = db.Column(db.String, nullable=False)    
    preco = db.Column(db.Integer, nullable=False)
    quartos = db.Column(db.Integer, nullable=False)
    area_total = db.Column(db.String(5), nullable=False)
    area_construida = db.Column(db.String(5), nullable=False)
    area_gourmet = db.Column(db.Integer, nullable=False)
    valor_entrada = db.Column(db.Integer, nullable=False)
    id_corretor = db.Column(db.Integer, db.ForeignKey('corretores.id'), nullable=False)
    corretor = db.relationship('Corretor', backref='imoveis')
    
    
    def __repr__(self):
        return f'<Imovel {self.regiao}, R${self.preco}>'