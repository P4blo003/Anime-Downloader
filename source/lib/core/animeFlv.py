# ---- MÓDULOS ---- #
from typing import List, Tuple

from lib.config.schema import AnimeFlvConfig

from bs4 import BeautifulSoup
import ast

from lib.core.anime import BaseAnime, BaseEpisode

from lib.common.network import get_html
from lib.common.types.string import clear_str
from lib.common.network import url_join


# ---- CLASES ---- #
class AnimeFlv_Episode(BaseEpisode):
    """
    Representa a un episodio de anime flv. Contiene la información y funciones.
    """
    # -- Métodos por defecto -- #
    def __init__(self, episode_id:int, episode_num:int):
        """
        Inicializa las propiedades.

        Args:
            episode_id (int): ID del episodio.
            episode_num (int): Número del episodio.
        """
        # Inicializa las propiedades.
        self.__id:int = episode_id
        super().__init__(episode_num=episode_num)           # Constructor clase base.
    

    # -- Propiedades -- #
    @property
    def Id(self) -> int:
        """
        Devuelve el ID del episodio.

        Returns:
            int: El ID del episodio.
        """
        return self.__id


class AnimeFlv_Anime(BaseAnime):
    """
    Representa a un anime de anime flv. Contiene la información y funciones.
    """
    # -- Métodos por defecto -- #
    def __init__(self, url:str):
        """
        Inicializa la instancia.

        Args:
            url (str): URL de la página inicial del anime.
        """
        # Inicializa las propiedades.
        self.__url:str = url
        self.__id:int = None
        self.__load_from_html()             # Carga los datos del html.
    

    # -- Propiedades -- #
    @property
    def Id(self) -> int:
        """
        Devuelve el ID del anime.

        Returns:
            int: El ID del anime.
        """
        return self.__id

    @property
    def Url(self) -> str:
        """
        Devuelve la URL de la página inicial del anime.

        Returns:
            str: La URL de la página inicial del anime.
        """
        return self.__url
    

    # -- Métodos privados -- #
    def __load_from_html(self) -> any:
        """
        Carga todos los datos del html.
        """
        # Obtiene el html.
        soup:BeautifulSoup = get_html(url=self.Url)

        # Obtiene el título del anime.
        title:str = soup.select_one("h1.Title").text

        # Obtiene la descripción del anime.
        description:str = soup.select_one("div.Description p").text

        # Obtiene los temas del anime.
        themes:List[str] = []
        themes_comp_list = soup.select("nav.Nvgnrs a")  # Obtiene los componentes
        # Para cada componente encontrado.
        for theme_comp in themes_comp_list:
            themes.append(theme_comp.text)  # Obtiene el texto.

        # Obtiene los episodios del anime.
        episodes:List[AnimeFlv_Episode] = []
        script_comp_list = soup.select("script")        # Obtiene los componentes <script>
        # Para cada componente encontrado.
        for script_comp in script_comp_list:
            if "var episodes" in script_comp.text:      # Si contiene ese valor en el texto.
                lines:List[str] = [clear_str(line) for line in str(script_comp.text).split(";") if line]    # Separa las líneas del script.
                anime_info_line:str = lines[0]
                episode_info_line:str = lines[1]
                # Convierte las cadenas en listas.
                anime_info_list = ast.literal_eval(anime_info_line.split('=', 1)[1].strip())
                episode_info_list = ast.literal_eval(episode_info_line.split('=', 1)[1].strip())

                # Asigna la información del anime.
                self.__id = int(anime_info_list[0])     # Obtiene el ID del anime.

                # Añade los episodios del anime.
                for episode_info in episode_info_list:
                    episodes.append(AnimeFlv_Episode(episode_id=episode_info[1], episode_num=episode_info[0])) # Añade el episodio.

        # Inicialia los parámetros de la clase base.
        super().__init__(title=title, description=description, themes=themes, episodes=episodes)        


class AnimeFlv:
    """
    Clase que contiene las funcionalidades relacionadas cohttps://www3.animeflv.net/n anime flv.
    """
    # -- Métodos por defecto -- #
    def __init__(self, cfg:AnimeFlvConfig=AnimeFlvConfig()):
        """
        Inicializa la instancia.

        Args:
            cfg (AnimeFlvConfig): Configuración con los parámetros de AnimeFlv.
        """
        # Inicializa las propiedades.
        self.__cfg:AnimeFlvConfig = cfg


    # -- Métodos públicos -- #
    def find_anime(self, name:str) -> List[Tuple[str, str]]:
        """
        Busca un anime en función del nombre dado y devuelve una lista con el nombre
        y la URL de la página inicial de cada uno.

        Args:
            name (str): El nombre del anime a buscar.
        
        Returns:
            List[Tuple[str,str]]: Una lista con tuplas. Cada tupla representa un anime encontrado
            la cual contiene el nombre `index=0` y la URl de la página inicial `index=1`.
        """
        # Variable a devolver.
        result:List[Tuple[str, str]] = []

        # Obtiene la query.
        query:str = generate_query(name=name)

        # Genera la URL completa.
        url:str = url_join(self.__cfg.base_url, "browse?q=")
        url += query        # Añade la query a la URL.

        # Obtiene el html.
        soup:BeautifulSoup = get_html(url=url)

        # Busca los componentes donde se almacena la información de los animes.
        anime_comp_list = soup.select("ul.ListAnimes li")   # Obtiene los li donde se almacenan los animes.
        # Para cada componente encontrado.
        for anime_comp in anime_comp_list:
            title:str = anime_comp.select_one("div.Title").text                                 # Obtiene el título del anime.
            anime_url:str = url_join(self.__cfg.base_url, anime_comp.select_one("a")["href"])   # Obtiene la URL.
            result.append((title, anime_url))                                                   # Añade los datos obtenidos.

        # Devuelve los resultados encontrados.
        return result


# ---- FUNCIONES ---- #
def generate_query(name:str) -> str:
    """
    Genera la query par el nombre de un anime dado.

        - Dado `name='Dragon Ball'` el resultado es `dragon+ball`.
    
    Args:
        name (str): El nombre del anime.
    """
    # Variable a devolver.
    query:str = ""

    # Preprocesa el nombre del anime.
    name = clear_str(value=name).lower()

    # Obtiene las palabras de la cadena.
    words:List[str] = name.split(" ")

    # Comprueba el número de palabras.
    if len(words) >= 1:
        query += words[0]   # Añade la primera palabra.

        # Comprueba que haya más de una palabra.
        if len(words) > 1:
            # Para cada palabra restante.
            for word in words:
                query += f'+{word}'     # Añade la palabra.
    
    # Devuelve la query generada.
    return query