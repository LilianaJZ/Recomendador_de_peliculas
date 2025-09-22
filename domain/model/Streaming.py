class Streaming:
    def __init__(self, id_stream, fecha_repr, pelicula, usuario, like):
        self._id_stream = id_stream
        self._fecha_repr = fecha_repr
        self._pelicula = pelicula
        self._usuario = usuario
        self._like = like

    # --- Propiedad para 'id_stream' ---
    @property
    def id_stream(self):
        return self._id_stream

    @id_stream.setter
    def id_stream(self, nuevo_id):
        self._id_stream = nuevo_id

    # --- Propiedad para 'fecha_repr' ---
    @property
    def fecha_repr(self):
        return self._fecha_repr

    @fecha_repr.setter
    def fecha_repr(self, nueva_fecha):
        self._fecha_repr = nueva_fecha

    # --- Propiedad para 'pelicula' ---
    @property
    def pelicula(self):
        return self._pelicula

    @pelicula.setter
    def pelicula(self, nueva_pelicula):
        self._pelicula = nueva_pelicula


    ###################################

    # --- Propiedad para 'usuario' ---
    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, nuevo_usuario):
        self._usuario = nuevo_usuario

    # --- Propiedad para 'like' ---
    @property
    def like(self):
        return self._like

    @like.setter
    def like(self, nuevo_like):
        self._like = nuevo_like