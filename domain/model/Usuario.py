class Usuario:


    def __init__(self, id, nombre, correo, contrasena):
        self._id = id
        self._nombre = nombre
        self._correo = correo
        self._contrasena = contrasena


    # Getter and Setter
    # --- Propiedad para 'id' ---
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    # --- Propiedad para 'nombre' ---
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    # --- Propiedad para 'correo' ---
    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, correo):
        self._correo = correo

    # --- Propiedad para 'contrasena' ---
    @property
    def contrasena(self):
        return self._contrasena

    @contrasena.setter
    def contrasena(self, contrasena):
        self._contrasena = contrasena