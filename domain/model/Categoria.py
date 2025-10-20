class Categoria:
    def __init__(self, id_categoria, categoria):
        self.__id_categoria = id_categoria
        self.__categoria = categoria

    # --- Propiedad para 'id_categoria' ---
    @property
    def id_categoria(self):
        return self.__id_categoria

    @id_categoria.setter
    def id_categoria(self, id_categoria):
        self.__id_categoria = id_categoria

    # --- Propiedad para 'categoria' ---
    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, categoria):
        self.__categoria = categoria

    @staticmethod
    def from_row(row):
        return Categoria(row[0], row[1])

#Metodo que nos convierte en imprimible cualquier valor que venga
    def __str__(self):
        return f"Categoria(id_categoria ={self.id_categoria}, nombre_categoria={self.categoria})"
#Metodo que organiza lo que le devuelva
    def __repr__(self):
        return self.__str__()