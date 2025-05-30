# ---- MÓDULOS ---- #
from abc import ABC
from typing import List, Tuple

from dataclasses import dataclass, field

from abc import abstractmethod


# ---- CLASES ---- #
@dataclass
class Anime:
    """
    Clase base que representa un anime. Contiene la información y métodos base.

    Attributes:
        Name (str): Nombre del anime.
        Description (str): Descripción del anime.
    """
    # -- Propiedades -- #
    __name:str = field(init=False, repr=False)
    __description:str = field(init=False, repr=False)


    # -- Métodos por defecto -- #
    def __init__(self, name:str, description:str, themes:List[str]):
        """
        Inicializa la instancia.

        Args:
            name (str): Nombre del anime.
            description (str): Descripción del anime.
            themes (List[str]): Listado con los temas del anime.
        """
        # Inicializa las propiedades.
        self.__name:str = name
        self.__description:str = description
        self.__themes:List[str] = themes
    
    def __repr__(self) -> str:
        """
        Devuelve la representación en cadena del objeto.

        Returns:
            str: Representación en cadena del objeto.
        """
        # Variable a devolver.
        strfmt:str = f"· Name: {self.Name}\n· Description: {self.Description}\n· Temas: "
        
        # Comrpueba que haya algún tema en el anime.
        if len(self.Themes):
            strfmt += f" {self.Themes[0]}"      # Añade el tema.
            # Comprueba que haya más de un tema que añadir.
            if len(self.Themes) > 1:
                # Para cada tema restante.
                for theme in self.Themes[1:]:
                    strfmt += f" | {theme}"     # Añade el tema.
        
        # Retorna la cadena.
        return strfmt


    # -- Propiedades -- #
    @property
    def Name(self) -> str:
        """
        Retorna el nombre del anime.

        Returns:
            str: El nombre del anime.
        """
        # Retorna el valor.
        return self.__name
    
    @property
    def Description(self) -> str:
        """
        Devuelve la descripción del anime.

        Returns:
            str: Descripción del anime.
        """
        return self.__description
    
    @property
    def Themes(self) -> List[str]:
        """
        Devuelve el listado con los temas del anime.

        Returns:
            List[str]: Listado con los temas del anime.
        """
        return self.__themes


class AnimeManager:
    """
    Clase base que representa un manager. Los managers son clases que contienen funciones
    para listar, descargar, etc. animes de páginas web.
    """
    # -- Métodos por defecto -- #
    def __init__(self):
        """
        Inicializa la instancia.
        """
        pass


    # -- Metodos abstractos -- #
    @abstractmethod
    def find_animes(self, name:str) -> List[Tuple[str, str]]:
        """
        Busca los animes disponibles a partir de un nombre dado. Devuelve un listado con tuplas.
            Cada tupla esta formada por:
            - index 0 = Nombre del anime.
            - index 1 = URL del anime.

        Args:
            name (str): El nombre del anime a buscar.

        Returns:
            List[Tuple[str,str]]: El listado con la información encontrada.
        """
        pass

    @abstractmethod
    def load_anime(self, url:str) -> Anime:
        """
        A partir de la URL de la página inicial de un Anime. Carga todos los datos del mismo.

        Args:
            url (str): URL de la página inicial del Anime.
        
        Returns:
            Anime: Instancia con la información del Anime.
        """
        pass


# ---- FUNCIONES ---- #
def query_from_name(name:str) -> str:
    """
    Genera la query del nombre. Este valor vale para las webs de AnimeFlv y AnimeFenix.
    
    Args:
        name (str): El nombre del anime para generar la query.
    
    Returns:
        str: La query generada.
    
    Examples:
        - 'Dragon Ball 2' -> 'dragon+ball+2'.
    """
    # Variable a devolver.
    query:str = ""

    # Genera la query.
    words:List[str] = name.split(" ")           # Separa el nombre por palabras.
    # Comprueba que haya palabras que añadir.
    if len(words) >= 1:
        query = words[0]                        # Añade la primera palabra.
        # Comprueba que haya más de 1 palabra para añadir.
        if len(words) > 1:
            # Para cada palabra restante.
            for word in words[1:]:
                query += f"+{word}"             # Añade la palabra.
    
    # Retorna la query generada.
    return query