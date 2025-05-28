# ---- CLASES ---- #
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
        self.__homeUrl:str = home_url
    
    
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
    

    # -- Métodos públicos -- #
    def download_episode(episode_index:int, dir:str) -> bool:
        """
        Decarga el anime con el índice especificado en el directorio.

        Args:
            episode_index (int): Índice del episodio.
            dir (str): Directorio donde almacenar el episodio.
        
        Returns:
            bool: True si se ha descargado correctamente y False en otro caso.
        """
        pass

    def download_all(dir:str) -> any:
        """
        Descarga todos los episodios del anime en el directorio.

        Args:
            dir (str): Directorio donde almacenar el episodio.
        """
        pass