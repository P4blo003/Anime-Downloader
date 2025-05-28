# ----------------------------------------------------------------------------------------
# · Filename: animeFlv.py
# · Author: Pablo González García.
# · Copyright (c) 2025 Pablo González García. All rights reserved.
# · Created on: 2025-05-27
# · Descripción: Módulo clases para gestionar los animes de AnimeFlv.
# ----------------------------------------------------------------------------------------


# ---- MÓDULOS ---- #
from typing import List

from bs4 import BeautifulSoup

import ast

from lib.common.network import get_html
from lib.common.string import clear_str


# ---- PARAMETROS ---- #
BASE_URL:str = "https://www3.animeflv.net"      # URL base.
BROWSE_URL:str = f"{BASE_URL}/browse"           # URL empleada para peticiones.
QUERY_URL:str = f"{BROWSE_URL}?q="              # URL para las querys.
WATCH_URL:str = f"{BASE_URL}/ver/"              # URL para ver un episodio.


# ---- CLASES ---- #
class Server:
    """
    Instancia que representa el servidor de descarga de un episodio de anime. Contiene toda la información
    y funciones.
    """
    # -- Métodos por defecto -- #
    def __init__(self, name:str, url:str):
        """
        Inicializa la instancia.

        Args:
            name (str): Nombre del servidor.
            url (str): URL del servidor.
        """
        # Inicializa los parámetros.
        self.__name:str = name
        self.__url:str = url
    
    def __repr__(self):
        """
        Retorna la representación del objeto en string.

        Returns:
            str: Representación del objeto en string.
        """
        return f"NAME: {self.Name} | URL: {self.Url}"


    # -- Propiedades -- #
    @property
    def Name(self) -> str:
        """
        Devuelve el nombre del servidor.

        Returns:
            str: Nombre del servidor.
        """
        return self.__name
    
    @property
    def Url(self) -> str:
        """
        Devuelve la URL de descarga del servidor.

        Returns:
            str: La URL de descarga del servidor.
        """
        return self.__url


class Episode:
    """
    Instancia que representa el episodio de un anime. Contiene toda la información y 
    funciones.
    """
    # -- Métodos por defecto -- #
    def __init__(self, episode_num:int, episode_id:int, watch_base_url:str):
        """
        Inicializa la instancia.
        
        Args:
            episode_num (int): El número el episodio.
            episode_id (int): El identificador del episodio.
            watch_base_url (str): URL base para ver el anime.
        """
        # Inicializa las propiedades.
        self.__id:int = episode_id
        self.__num:int = episode_num
        self.__title:str = f"Episodio-{episode_num}"
        self.__watchUrl:str = f"{watch_base_url}-{self.Num}"
        self.__downloadServers:List[Server] = []
    
    def __repr__(self):
        """
        Retorna la representación del objeto en string.

        Returns:
            str: Representación del objeto en string.
        """
        return f"{self.Title} | ID: {self.Id} | WATCH: {self.WatchUrl}"
    
    
    # -- Propiedades -- #
    @property
    def Title(self) -> str:
        """
        Devuelve el título del episodio.

        Returns:
            str: El título del episodio.
        """
        return self.__title
    
    @property
    def Num(self) -> int:
        """
        Obtiene el número del episodio.

        Returns:
            int: Número del episodio.
        """
        return self.__num
    
    @property
    def Id(self) -> int:
        """
        Devuelve el id del episodio.

        Returns:
            int: Id del episodio.
        """
        return self.__id

    @property
    def WatchUrl(self) -> str:
        """
        Devuelve la URL para ver el anime.

        Returns:
            str: La URL para ver el anime.
        """
        return self.__watchUrl
    
    @property
    def DownloadServers(self) -> List[Server]:
        """
        Devuelve el listado con los servidores de descarga.

        Returns:
            List[Server]: Listado con los servidores de descarga.
        """
        return self.__downloadServers


    # -- Métodos públicos -- #
    def load_download_servers(self) -> any:
        """
        Carga el listado de servidores disponibles para descargar el anime.
        """
        # Reinicia el listado de los servidores.
        self.__downloadServers = []

        # Obtiene el HTML.
        soup:BeautifulSoup = get_html(url=self.WatchUrl)

        # Obtiene los servidores.
        servers = soup.select("table.RTbl tbody tr")
        for server in servers:
            server_name:str = server.select_one("td").text
            server_url:str = server.select_one("td a.fa-download")["href"]
            self.__downloadServers.append(Server(name=server_name, url=server_url))

class Anime:
    
    """
    Instancia que representa un anime. Contiene toda la información y funciones.
    """
    # -- Métodos por defecto -- #
    def __init__(self, name:str, home_url:str):
        """
        Inicializa la instancia.

        Args:
            name (str): Nombre del anime.
            home_url (str): URl de la página inicial del anime.
        """
        # Inicializa las propiedades.
        self.__name:str = name
        self.__homeUrl:str = f"{BASE_URL}{home_url}"
        self.__episodes:List[Episode] = []
    
    def __repr__(self) -> str:
        """
        Retorna la representación del objeto en string.

        Returns:
            str: Representación del objeto en string.
        """
        return f"NAME: {self.Name} | URL: {self.HomeUrl}"
    
    
    # -- Propiedades -- #
    @property
    def Name(self) -> str:
        """
        Devuelve el nombre del anime.

        Returns:
            str: Nombre del anime.
        """
        return self.__name
    
    @property
    def HomeUrl(self) -> str:
        """
        Devuelve la URL de la página de inicio del anime.

        Returns:
            str: La URL de la página de inicio del anime.
        """
        return self.__homeUrl
    
    @property
    def Episodes(self) -> List[Episode]:
        """
        Devuelve el listado de episodios del anime.

        Returns:
            List[Episode]: Listado con los episodios del anime.
        """
        return self.__episodes
    

    # -- Métodos públicos -- #
    def load_episodes(self) -> any:
        """
        Obtiene el listado de episodios.
        """
        self.__episodes = get_episodes(url=self.HomeUrl)


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
        pass
    

    # -- Métodos públicos -- #
    def list_animes(self, max_pages:int) -> List[Anime]:
        """
        Lista los animes disponibles. En caso de que se pase un valor
        de `max_pages`, solo se buscarán los animes para ese número de
        páginas.

        Args:
            max_pages (int): Número de páginas a comprobar.

        Returns:
            List[Anime]: Listado con los animes encontrados.
        """
        # Obtiene el HTML.
        pass

    def find_anime(self, query:str) -> List[Anime]:
        """
        Busca un anime por el nombre y devuelve los resultados obtenidos.

        Args:
            query (str): Nombre del anime a buscar.
        
        Raises:
            NetworkBadResponseError: En caso de que el estado de la petición no sea 200.
        
        Returns:
            List[Anime]: Anime encontrado.
        """
        # Valor a devolver.
        results:List[Anime] = []

        # Obtiene la URL para buscar el anime.
        url:str = generate_search_url(query=query)

        # Obtiene el HTML.
        soup:BeautifulSoup = get_html(url=url)

        # Obtiene los animes encontrados.
        anime_list = soup.select("ul.ListAnimes li")
        for anime in anime_list:
            title:str = anime.select_one("div.Title").text          # Obtiene el título.
            base_url:str = anime.select_one("a")["href"]            # Obtiene la URL base.
            results.append(Anime(name=title, home_url=base_url))    # Añade el anime a la lista.     
        
        # Retorna el resultado.
        return results

# ---- FUNCIONES ---- #
def process_query(query:str) -> str:
    """
    Procesa la query y la devuelve en el formato correcto para buscar
    animes en AnimeFlv.
    """
    # Variable a devolver.
    result:str = ''

    # Separa las palabras de la cadena y las formatea a minúsculas.
    words = [str(word).lower() for word in query.split(' ')]

    # Comprueba que haya palabras que añadir.
    if len(words) >= 1:
        result += words[0]  # Añade la primera palabra.

        # Comprueba que haya más palabras que añadir.
        if len(words) > 1:
            # Para cada palabra.
            for word in words[1:]:
                result += f'+{word}'    # Añade la palabra.
    
    # Retorna el resultado.
    return result


def generate_search_url(query:str) -> str:
    """
    Genera la url para buscar un anime.

    Args:
        query (str): Query introducida por el usuario.
    
    Returns:
        str: La URL completa para buscar el anime.
    """
    # Preprocesa el nombre.
    query = clear_str(value=query)      # Limpia la cadena.
    query = process_query(query=query)  # Procesa la query y la devuelve en el formato correcto.

    # Genera la URL.
    url:str = f"{QUERY_URL}{query}"

    # Retorna la URL generada.
    return url


def get_episodes(url:str) -> List[Episode]:
    """
    Obtiene un listado con los episodios para la URL dada.

    Args:
        url (str): URl a la que hacer la petición.
    
    Raises:
        NetworkBadResponseError: En caso de que el estado de la petición no sea 200.

    Returns:
        List[Episode]: Listado con los episodios.
    """
    # Variable a devolver.
    result:List[Episode] = []

    # Obtiene el HTML.
    soup:BeautifulSoup = get_html(url=url)

    # Obtiene el listado de episodios.
    scripts = soup.select("script")         # Obtiene los scripts.
    for script in scripts:
        if 'var episodes' in script.text:        # Si contiene información de los episodios.
            content:str = clear_str(value=script.text)
            values = content.split(";")

            # Obtiene la información del anime.
            anime_info:List[str] = values[0].split("var anime_info = ")
            anime_list:List[str] = ast.literal_eval(anime_info[1])
            url:str = f"{WATCH_URL}{anime_list[2]}"

            # Obtiene la información de los episodios.
            values = values[1].split("var episodes = [")
            data:str = values[1][:-1]
            data_list = ast.literal_eval("[" + data + "]")
            for tuple in data_list:
                result.append(Episode(episode_num=tuple[0], episode_id=tuple[1], watch_base_url=url))
    
    # Retorna el listado de episodios.
    return result