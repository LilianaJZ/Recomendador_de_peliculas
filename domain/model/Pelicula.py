class Pelicula:

    # se nombra un constructor y dentro de ese construcctor se inicializan
    # los atributos de la clase

    def __init__(self, id, titulo, anio, calificacion, duracion, descripcion, estado, director):
        self.__id = id #se utiliza la palabra reservada self que es igual al this en java
        self.__titulo = titulo
        self.__anio = anio
        self.__calificacion = calificacion
        self.__duracion = duracion
        self.__descripcion = descripcion
        self.__estado = estado
        self.__director = director



    #En python _ es para proteger el parámetro (protected)
    # __ es para privado (solo lo ve la clase y el paquete)
    #sin nada es public

    #Getter and Setter (encapsulamiento)
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def anio(self):
        return self.__anio

    @anio.setter
    def anio(self, anio):
        self.__anio = anio

    @property
    def calificacion(self):
        return self.__calificacion

    @calificacion.setter
    def calificacion(self, calificacion):
        self.__calificacion = calificacion

    @property
    def duracion(self):
        return self.__duracion

    @duracion.setter
    def duracion(self, duracion):
        self.__duracion = duracion

    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        self.__descripcion = descripcion

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, estado):
        self.__estado = estado

    @property
    def director(self):
        return self.__director

    @director.setter
    def director(self, director):
        self.__director = director


    # polimorfismo por sobreescritura de objetos
    # si un lenguaje es orientado a objetos el concepto por detrás es
    # exactamente el mismo


    #Tipos de relaciones entre clases:
    #Hay 3 tipos:
    #Relaciones de herencia
    # relciones de asosciacion por composici[on: Cuando una clase no puede existir si no hya un usuario que genere esa composicion
    #relaciones de asociaci[on por agregacion : las dos clases pueden existir independiente de la otra

    ##Métodos propios
