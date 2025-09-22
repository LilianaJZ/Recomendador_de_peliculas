from  domain.model import Usuario

class Usuario_Free(Usuario):
    def __init__(self, id, nombre, correo, contrasena, flag_free, ads):
        super.__init__(id, nombre, correo, contrasena)
        self.__flag_free = flag_free
        self.__ads = ads

    ## Getter and Setter

    '''
    TAREA:
    -Hacer los getter y setter 
    -llenar las clases que hacen falta
    -Dividir los servicios (tienen los metodos que tienen la logica)
    
    '''

    # --- Property for 'flag_free' ---
    @property
    def flag_free(self):
        return self.__flag_free

    @flag_free.setter
    def flag_free(self, flag_free):
        self.__flag_free = flag_free

    # --- Property for 'ads' ---
    @property
    def ads(self):
        return self.__ads

    @ads.setter
    def ads(self, ads):
        self.__ads = ads



