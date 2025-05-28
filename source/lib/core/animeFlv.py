# ---- MÓDULOS ---- #
from typing import List

from .base import Anime


# ---- CLASES ---- #
class AnimeFlv:
    """
    Clase encargada de gestionar todo lo relacionado con las acciones de anime flv. Es un
    único punto de entrada para las funciones.
    """
    # -- Métodos por defecto -- #
    def __init__(self):
        """
        Inicializa la instancia.
        """
        # Inicializa las propiedades.
    
    
    # -- Métodos públicos -- #
    def list_animes(max_pages:int) -> List[Anime]:
        """
        Lista los animes disponibles. En caso de que se pase un valor
        de `max_pages`, solo se buscarán los animes para ese número de
        páginas.

        Args:
            max_pages (int): Número de páginas a comprobar.

        Returns:
            List[Anime]: Listado con los animes encontrados.
        """
        pass

    def find_anime(anime_name:str) -> Anime:
        """
        Busca un anime por el nombre y devuelve el resultado.

        Args:
            anime_name (str): Nombre del anime a buscar.
        
        Returns:
            Anime: Anime encontrado.
        """
        pass