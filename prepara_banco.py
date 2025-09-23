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
               bairro TEXT NOT NULL
               cidade TEXT NOT NULL, 
               preco INTEGER NOT NULL,
               quartos INTEGER NOT NULL, 
               area_total TEXT NOT NULL,
               area_construida TEXT,
               area_gourmet TEXT NOT NULL CHECK(area_gourmet IN('Sim', 'Não')),
               Valor_entrada INTEGER,
                link_anuncio TEXT NOT NULL,
               id_corretor INTEGER NOT NULL, FOREIGN KEY(id_corretor) REFERENCES Corretores(id))
               
               ''')


cursor.execute("INSERT INTO Corretores (nome, Contato) VALUES ('Lourenço Imoveis', '(62) 98428-4002'),('Marcos Dias', '(62) 9154-0452') ")
cursor.execute(''' 
            INSERT INTO Imoveis(regiao, preco, quartos, area_total, area_construida, area_gourmet, valor_entrada, link_anuncio, id_corretor) values 
               ('Centro', 350000, 3, '120m²', '100m²', 'Não', 50000, 'https://colab.google/', 1),
               ('Setor Oeste', 450000, 4, '150m²', '120m²', 'Sim', 80000,  'https://www.google.com/anuncio2', 2) ,
               ('Jardim América', 300000, 3, '110m²', '90m²', 'Não', 60000, 'https://www.exemplo.com/anuncio3', 1)

 ''')


print(cursor.fetchall()) #

banco.commit()
banco.close()