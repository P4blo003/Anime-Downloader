# ---- CLASES ---- #
class AnimeFlvConfig:
    """
    Almacena la configuración de `AnimeFlv`.

    Attributes:
        base_url (str): URL base de animeFlv.
        browse_url (str): URL base para listar los animes disponibles.
        query_url (str): URL base para buscar animes.
        base_watch_url (str): URL base para ver episodios.
    """
    # -- Atributos -- #
    base_url:str    = "https://www3.animeflv.net"
    browse_url:str  = "https://www3.animeflv.net/browse"
    query_url:str   = "https://www3.animeflv.net/browse?q="
    watch_url:str   = "https://www3.animeflv.net/ver"


class AnimeFenixConfig:
    """
    Almacena la configuración de `Anime Fenix`.

    Attributes:
        base_url (str): URL base de animeFlv.
        browse_url (str): URL base para listar los animes disponibles.
        query_url (str): URL base para buscar animes.
        base_watch_url (str): URL base para ver episodios.
    """
    # -- Atributos -- #
    base_url:str    = "https://animefenix2.tv"
    browse_url:str  = "https://animefenix2.tv/directorio/anime"
    query_url:str   = "https://animefenix2.tv/directorio/anime?q="
    watch_url:str   = "https://animefenix2.tv/ver"