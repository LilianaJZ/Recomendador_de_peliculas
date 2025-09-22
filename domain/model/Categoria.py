class Categoria:
    def __init__(self, id_categoria, descripcion):
        self._id_categoria = id_categoria
        self._descripcion = descripcion

    # --- Propiedad para 'id_categoria' ---
    @property
    def id_categoria(self):
        return self._id_categoria

    @id_categoria.setter
    def id_categoria(self, id_categoria):
        self._id_categoria = id_categoria

    # --- Propiedad para 'descripcion' ---
    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        self._descripcion = descripcion