from encodings.punycode import selective_find

from domain.model.Categoria import Categoria


class Categoria_Service:
    def __init__(self):
        self.categoria = Categoria()
        self.categoria_repositorio = Categoria_Repositorio

    def crear_categoria(self):
        id = int(input("Ingrese el nombre de  la categoria: "))
        self.categoria = nombre_categoria
