from persistence.Conexion import conexion

class Pelicula_Repositorio:

    def __init__(self):
        self.db = conexion ( host='localhost', port=3306, uer='root', password="", database='movie_recomender_DB' )
        self.db.connect()


    def crear_pelicula(self):
        query = """INSERT INTO """