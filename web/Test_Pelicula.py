from domain.model.Categoria import Categoria
from domain.model.Pelicula import Pelicula
from domain.service.Pelicula_Service import Pelicula_Service


class Test_Pelicula:

    categoria = Categoria(None,None)
    pelicula = Pelicula(None,None,None,None,None,None,None,None,None)
    pelicula_service = Pelicula_Service()



    pelicula_service.crear_pelicula(pelicula,categoria)