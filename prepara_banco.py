import sqlite3

banco = sqlite3.connect("imovel.db") #variavel para criar ou se conectar com o banco

#cria a variavel cursor que vai receber o objeto banco e irá utilizar o metodo cursor que vai nos possibilitar criar tabelas e manipular o banco de dados 

cursor = banco.cursor()


# cursor.execute('''CREATE TABLE corretores (
#                id INTEGER PRIMARY KEY AUTOINCREMENT,
#                nome TEXT NOT NULL,
#                Contato TEXT NOT NULL
#                )''')

# cursor.execute('''CREATE TABLE Imoveis(
#                id INTEGER PRIMARY KEY AUTOINCREMENT,
#                regiao TEXT NOT NULL, 
#                preco INTEGER NOT NULL,
#                quartos INTEGER, 
#                area_total TEXT ,
#                area_construida TEXT,
#                area_gourmet TEXT NOT NULL CHECK(area_gourmet IN('Sim', 'Não')),
#                Valor_entrada INTEGER,
#                id_corretor INTEGER NOT NULL,
#                FOREIGN KEY(id_corretor) REFERENCES corretores(id)
#                )
#                ''')


cursor.execute("INSERT INTO corretores (nome, Contato) VALUES ('Lourenço Imoveis', '(62) 98428-4002')")
cursor.execute(''' SELECT * from corretores''')

print(cursor.fetchall()) #

banco.commit()
banco.close()