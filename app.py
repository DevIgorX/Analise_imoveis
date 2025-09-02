from flask import Flask, render_template

# Cria a nossa aplicação
app = Flask(__name__)



imoveis = [
    {
        "id": 1,
        "endereco": "Rua das Flores, 123, Bairro Jardim",
        "preco": "R$ 350.000,00",
        "link": "http://site-de-anuncios.com/1",
        "corretor": "Maria Silva",
        "telefone_corretor": "(62) 99999-1111"
    },
    {
        "id": 2,
        "endereco": "Avenida Principal, 456, Setor Central",
        "preco": "R$ 480.000,00",
        "link": "http://outro-site.com/2",
        "corretor": "João Costa",
        "telefone_corretor": "(62) 98888-2222"
    }
]



@app.route('/')
def ola_mundo():
    return render_template('index.html', lista_de_imoveis=imoveis)

# Adição para rodar o app diretamente
if __name__ == '__main__':
    app.run(debug=True)