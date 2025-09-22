'''
Clase con los metodos que se van a usar
se puede hacer un constructor e inicializar pelicula

pelicula va a ser un objeto y aqui se pone la logica que va a tener el codigo
'''

class Pelicula_Service:

    #inyeccion de dependencias, donde recibo un objeto
    def __init__(self, pelicula):
        self.pelicula = pelicula

    #aqui se inicializa el objeto y se le dan valores
    def crear_pelicula(self, pelicula):
        id = int(input("Ingrese el ID de la pelicula: "))
        self.pelicula.id = id #este es el set
        titulo = int(input("Ingrese el nombre de la pelicula: "))
        self.pelicula.titulo = titulo  # este es el set
        anio = int(input("Ingrese el anio de la pelicula: "))
        self.pelicula.anio = anio
        calificacion = int(input("Ingrese el calificacion de la pelicula: "))
        self.pelicula.calificacion = calificacion
        duracion = int(input("Ingrese el duracion de la pelicula: "))
        self.pelicula.duracion = duracion
        estado = int(input("Ingrese el estado de la pelicula: "))
        self.pelicula.estado = estado
        categorie = int(input("Ingrese el categoria de la pelicula: "))
        self.pelicula.categorie = categorie
        director = int(input("Ingrese el director de la pelicula: "))
        self.pelicula.director = director


    def listar_peliculas(self):
        return self.pelicula

    def buscar_pelicula(self, id):
        return self.pelicula.id

    def actualizar_pelicula(self, pelicula):
        id = int(input("Ingrese el ID de la pelicula: "))

    def eliminar_pelicula(self, id):
        id = int(input("Ingrese el ID de la pelicula: "))