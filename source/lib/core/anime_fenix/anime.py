# ---- MÓDULOS ---- #
from typing import List, Tuple

from lib.config.schema import AnimeFenixConfig

from lib.core.anime import Anime, AnimeManager
from lib.core.anime import query_from_name

from lib.common.network import get_html, url_join
from lib.common.types.string import clear_str

from dataclasses import field


# ---- CLASES ---- #
class AnimeFenixManager(AnimeManager):
    """
    Clase que representa la instancia del manager para la web de `AnimeFenix`.

    Attributes:
        cfg (AnimeFenixConfig): Configuración de AnimeFlv.
    """
    # -- Propiedades -- #
    __cfg:AnimeFenixConfig = field(init=False, repr=False)


    # -- Métodos por defecto -- #
    def __init__(self, cfg:AnimeFenixConfig=AnimeFenixConfig()):
        """
        Inicializa la instancia.

        Args:
            cfg (AnimeFenixConfig): Configuración de AnimeFlv.
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
        anime_comp_list = html.select("ul.grid-animes li")
        # Para cada componente encontrado.
        for anime_comp in anime_comp_list:
            # Obtiene el nombre y la URL base.
            comp = anime_comp.select("article a p")
            title:str = comp[len(comp)-1].text                              # El último <p> es el título.
            base_url:str = anime_comp.select_one("article a")["href"]

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
        anime:Anime = None

        # Obtiene el HTML.
        html = get_html(url=url)

        # Obtiene el nombre del anime.
        title:str = html.select_one("h1.text-orange-500").text

        # Obtiene la descripción del anime.
        description:str = html.select_one("div.mb-6 p.text-gray-300").text

        # Obtiene los temas del anime.
        themes:List[str] = []           # Genera el listado inicial.
        theme_comp_list = html.select("div.mb-6 div a.duration-300")
        # Para cada componente encontrado.
        for theme_comp in theme_comp_list:
            themes.append(clear_str(theme_comp.text))  # Añade el tema.
        
        # Crea el anime con los datos.
        anime = Anime(name=title, description=description, themes=themes)
        
        # Retorna el anime.
        return anime