# ----------------------------------------------------------------------------------------
# · Filename: string.py
# · Author: Pablo González García.
# · Copyright (c) 2025 Pablo González García. All rights reserved.
# · Created on: 2025-05-30
# · Descripción: Módulo con clases y funciones encargadas para los animes.
# ----------------------------------------------------------------------------------------


# ---- MÓDULOS ---- #
from typing import List

from lib.common.types.int import int_to_str


# ---- CLASES ---- #
class BaseEpisode:
    """
    Representa el episodio de un anime. Almacena la información del mismo y las
    funciones.
    """
    # -- Métodos por defecto -- #
    def __init__(self, episode_num:int):
        """
        Inicializa la instancia.

        Args:
            episode_num (int): El número del episodio.
        """
        # Inicializa las propiedades.
        self.__episodeNum:int = episode_num
        self.__name:str = f"ep_{int_to_str(num=self.EpisodeNum, result_length=5)}"
    
    def __repr__(self) -> str:
        """
        Genera la representación en cadena del objeto.

        Returns:
            str: La representación en cadena del objeto.
        """
        # Variable a devolver.
        strfmt:str = f"NAME: {self.Name}"

        # Retorna la cadena generada.
        return strfmt
    

    # -- Propiedades -- #
    @property
    def EpisodeNum(self) -> int:
        """
        Devuelve el número de episodio.

        Returns:
            int: El número del episodio.
        """
        return self.__episodeNum
    
    @property
    def Name(self) -> str:
        """
        Devuelve el nombre del episodio.

        Returns:
            str: El nombre del episodio.
        """
        return self.__name


class BaseAnime:
    """
    Representa a un anime. Almacena la información del mismo y las funciones.
    """
    # -- Métodos por defecto -- #
    def __init__(self, title:str, description:str, themes:List[str], episodes:List[BaseEpisode]):
        """
        Inicializa la instancia.

        Args:
            title (str): El título del anime.
            description (str): La descripción del anime.
            themes (List[str]): Lista con los temas del anime.
            episodes (List[BaseEpisode]): Lista con los episodios del anime.
        """
        # Inicializa las propiedades.
        self.__title:str = title
        self.__description:str = description
        self.__themes:List[str] = themes
        self.__episodes:List[BaseEpisode] = episodes

    def __repr__(self) -> str:
        """
        Genera la representación en cadena del objeto.

        Returns:
            str: La representación en cadena del objeto.
        """
        # Variable a devolver.
        strfmt:str = f"- TÍTULO: {self.Title}\n- DESCRIPCIÓN: {self.Description}\n- TEMAS: "

        # Añade los temas del anime.
        if len(self.Themes) >= 1:
            strfmt += self.Themes[0]
            # Si quedan más temas que añadir.
            if len(self.Themes) > 1:
                for theme in self.Themes[1:]:   # Para cada tema.
                    strfmt += f" | {theme}"     # Añade el tema.
        
        # Añade la información de los episodios.
        strfmt += f"\n- EPISODIOS: {len(self.Episodes)}\n"

        # Retorna la cadena generada.
        return strfmt


    # -- Propiedades --
    @property
    def Title(self) -> str:
        """
        Devuelve el título del anime.

        Returns:
            str: El título del anime.
        """
        return self.__title
    
    @property
    def Description(self) -> str:
        """
        Devuelve la descripción del anime.

        Returns:
            str: La descripción del anime.
        """
        return self.__description
    
    @property
    def Themes(self) -> List[str]:
        """
        Devuelve los temas del anime.

        Returns:
            List[str]: Los temas del anime.
        """
        return self.__themes
    
    @property
    def Episodes(self) -> List[BaseEpisode]:
        """
        Devuelve el listado con los episodios del anime.

        Returns:
            List[BaseEpisode]: El listado con los episodios del anime.
        """
        return self.__episodes