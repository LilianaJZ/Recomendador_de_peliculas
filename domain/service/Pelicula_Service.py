'''
Clase con los metodos que se van a usar
se puede hacer un constructor e inicializar pelicula

pelicula va a ser un objeto y aqui se pone la logica que va a tener el codigo
'''

from domain.model.Categoria import Categoria
from domain.service.Categoria_Service import Categoria_Service
from domain.model.Pelicula import Pelicula

class Pelicula_Service:

    #inyeccion de dependencias, donde recibo un objeto
    def __init__(self):
        self.pelicula = Pelicula(None, None, None, None, None, None, None, None, None)
        self.categoria = Categoria(None, None)
        self.categoria_service = Categoria_Service()

    #aqui se inicializa el objeto y se le dan valores. Se pasa el objeto de categoria para hacer la relacion
    def crear_pelicula(self, pelicula, categoria):
        id = int(input("Ingrese el ID de la pelicula: "))
        self.pelicula.id = id
        titulo = input("Ingrese el nombre de la pelicula: ")
        self.pelicula.titulo = titulo
        anio = input("Ingrese el año de estreno de la pelicula: ")
        self.pelicula.anio = anio
        calificacion = input("Ingrese el calificacion de la pelicula: ")
        self.pelicula.calificacion = calificacion
        duracion = input("Ingrese la duracion de la pelicula: ")
        self.pelicula.duracion = duracion
        estado = input("Ingrese la estado de la pelicula: ")
        self.pelicula.estado = estado
        self.categoria_service.mostrar_categorias()
        categoria = int(input("Ingrese el Id de la categoria de la pelicula: "))
        self.pelicula.categoria = categoria
        director = input("Ingrese el director de la pelicula: ")
        self.pelicula.director = director


    def listar_peliculas(self):
        return self.pelicula

    def buscar_pelicula(self, id):
        return self.pelicula.id

    def actualizar_pelicula(self, pelicula):
        id = int(input("Ingrese el ID de la pelicula: "))

    def eliminar_pelicula(self, id):
        id = int(input("Ingrese el ID de la pelicula: "))