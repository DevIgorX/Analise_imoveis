
# imoveis = [
#     {
#         "id": 1,
#         "endereco": "Rua das Flores, 123, Bairro Jardim",
#         "preco": "R$ 350.000,00",
#         "link": "https://www.instagram.com/p/DNovJNPJ2_P/?img_index=1",
#         "corretor": "Maria Silva",
#         "telefone_corretor": "(62) 99999-1111"
#     },
#     {
#         "id": 2,
#         "endereco": "Avenida Principal, 456, Setor Central",
#         "preco": "R$ 480.000,00",
#         "link": "https://www.instagram.com/p/DNlJ2uLOREZ/",
#         "corretor": "João Costa",
#         "telefone_corretor": "(62) 98888-2222"
#     }
# ]


class Imoveis:
    def __init__(self, endereco, preco,terreno_total, quartos, link, corretor, telefone_corretor):
        self.endereco = endereco
        self.preco = preco
        self.terreno_total = terreno_total
        self.quartos = quartos
        self.link = link
        self.corretor = corretor
        self.telefone_corretor = telefone_corretor


imovel1 = Imoveis("Rua das Flores, 123, Bairro Jardim", "R$ 350.000,00", "180m", 2,"https://www.instagram.com/p/DNovJNPJ2_P/?img_index=1", "Maria Silva", "(62) 98888-2222")
imovel2 = Imoveis("Avenida Principal, 456, Setor Central", "R$ 480.000,00", "200m", 3,"https://www.instagram.com/p/DNlJ2uLOREZ/", "João Costa", "(62) 98888-2255")


imoveis = [imovel1, imovel2]

