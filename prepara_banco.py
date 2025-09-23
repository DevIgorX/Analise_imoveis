import sqlite3

banco = sqlite3.connect("imovel.db") #variavel para criar ou se conectar com o banco

cursor = banco.cursor()


cursor.execute('''CREATE TABLE Corretores (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               Contato TEXT NOT NULL
               )''')

cursor.execute('''CREATE TABLE Imoveis(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               bairro TEXT NOT NULL,
               cidade TEXT NOT NULL, 
               estado TEXT NOT NULL DEFAULT 'Go',
               preco INTEGER NOT NULL,
               quartos INTEGER NOT NULL, 
               area_total TEXT NOT NULL,
               area_construida TEXT,
               area_gourmet TEXT NOT NULL CHECK(area_gourmet IN('Sim', 'Não')),
               suite TEXT NOT NULL CHECK(suite IN('Sim', 'Não')),
               Valor_entrada INTEGER,
                link_anuncio TEXT NOT NULL,
               id_corretor INTEGER NOT NULL, FOREIGN KEY(id_corretor) REFERENCES Corretores(id))
               
               ''')


cursor.execute("INSERT INTO Corretores (nome, Contato) VALUES ('Lourenço Imoveis', '(62) 98428-4002'),('Marcos Dias', '(62) 9154-0452') ")
cursor.execute(''' 
            INSERT INTO Imoveis(bairro, cidade, preco, quartos, area_total, area_construida, area_gourmet, suite , valor_entrada, link_anuncio, id_corretor) values 
               ('Centro','Goiânia', 350000, 3, '120m²', '100m²','Não','Sim', 50000, 'https://colab.google/', 1),
               ('Setor Oeste','Trindade', 450000, 4, '150m²', '120m²','Sim','Não', 80000,  'https://www.google.com/anuncio2', 2) ,
               ('Jardim América','Goiania', 300000, 3, '110m²', '90m²','Não','Sim', 60000, 'https://www.exemplo.com/anuncio3', 1)

 ''')


print(cursor.fetchall()) #

banco.commit()
banco.close()