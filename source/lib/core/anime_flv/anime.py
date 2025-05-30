# ---- MÓDULOS ---- #
from typing import List, Tuple

from lib.config.schema import AnimeFlvConfig

from lib.core.anime import Anime, AnimeManager
from lib.core.anime import query_from_name

from lib.common.network import get_html, url_join
from lib.common.types.string import clear_str

from dataclasses import field


# ---- CLASES ---- #
class AnimeFlvManager(AnimeManager):
    """
    Clase que representa la instancia del manager para la web de `AnimeFlv`.

    Attributes:
        cfg (AnimeFlvConfig): Configuración de AnimeFlv.
    """
    # -- Propiedades -- #
    __cfg:AnimeFlvConfig = field(init=False, repr=False)


    # -- Métodos por defecto -- #
    def __init__(self, cfg:AnimeFlvConfig=AnimeFlvConfig()):
        """
        Inicializa la instancia.

        Args:
            cfg (AnimeFlvConfig): Configuración de AnimeFlv.
        """
        # Inicializa las propiedades.
        self.__cfg = cfg
    

    # -- Métodos de AnimeManager -- #
    def find_animes(self, name) -> List[Tuple[str, str]]:
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
        # Variable a devolver.
        results:List[Tuple[str, str]] = []

        # Preprocesa el nombre.
        name = clear_str(value=name).lower()        # Limpia el nombre y lo pone en minúsculas.

        # Genera la query.
        query = query_from_name(name=name)

        # Genera la URL para la query.
        url:str = self.__cfg.query_url + query

        # Obtiene el HTML.
        html = get_html(url=url)

        # Obtiene los componentes donde esta la información de los animes.
        anime_comp_list = html.select("ul.ListAnimes li")
        # Para cada componente encontrado.
        for anime_comp in anime_comp_list:
            # Obtiene el nombre y la URL base.
            title:str = anime_comp.select_one("h3.Title").text
            base_url:str = anime_comp.select_one("article.Anime a")["href"]
            
            # Añade la tupla a la lista.
            results.append((title, url_join(self.__cfg.base_url, base_url)))
    
        # Retorna el resultado.
        return results

    def load_anime(self, url:str):
        """
        A partir de la URL de la página inicial de un Anime. Carga todos los datos del mismo.

        Args:
            url (str): URL de la página inicial del Anime.
        
        Returns:
            Anime: Instancia con la información del Anime.
        """
        # Variable a devolver.
        anime = None

        # Obtiene el HTML.
        html = get_html(url=url)

        # Obtiene el nombre del anime.
        title:str = html.select_one("h1.Title").text

        # Obtiene la descripción del anime.
        description:str = html.select_one("div.Description p").text

        # Obtiene los temas del anime.
        themes:List[str] = []               # Genera el listado inicial.
        theme_comp_list = html.select("nav.Nvgnrs a")
        # Para cada componente encontrado.
        for theme_comp in theme_comp_list:
            themes.append(theme_comp.text)  # Añade el tema.
        
        # Crea el anime con los datos.
        anime = Anime(name=title, description=description, themes=themes)
        
        # Retorna el anime.
        return anime