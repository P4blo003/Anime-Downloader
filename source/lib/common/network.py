# ----------------------------------------------------------------------------------------
# · Filename: network.py
# · Author: Pablo González García.
# · Copyright (c) 2025 Pablo González García. All rights reserved.
# · Created on: 2025-05-28
# · Descripción: Módulo con funciones encargadas para ayudar con las peticiones http.
# ----------------------------------------------------------------------------------------


# ---- MÓDULOS ---- #
from requests import get
from requests import Response
from bs4 import BeautifulSoup
from http import HTTPStatus


# ---- CLASES ---- #
class NetworkBadResponseError(Exception):
    """
    Excepción causada cuando el estado de la respuesta de una petición a una URL no sea 200.
    """
    # -- Métodos por defecto -- #
    def __init__(self, status_code:int, reason:str):
        """
        Inicializa la instancia.

        Args:
            status_code (int): Estado de la respuesta.
            reason (str): Motivo del estado de la respuesta.
        """
        # Inicializa las propiedades.
        self.__statusCode:int = status_code
        self.__reason:str = reason
        super().__init__(f"STATUS_CODE: {self.StatusCode} | REASON: {self.Reason}")       # Constructor de la clase Exception.
    

    # -- Propiedades -- #
    @property
    def StatusCode(self) -> int:
        """
        Devuelve el estado de la respuesta.

        Returns:
            int: Estado de la respuesta.
        """
        return self.__statusCode
    
    @property
    def Reason(self) -> str:
        """
        Devuelve el motivo del estado de la respuesta.

        Returns:
            str: Motivo del estado de la respuesta.
        """
        return self.__reason


# ---- FUNCIONES ---- #
def get_response(url:str) -> Response:
    """
    Realiza una petición GET a la URL dada.

    Args:
        url (str): URl a la que hacer la petición.
    
    Raises:
        NetworkBadResponseError: Causada si el estado de la respuesta no es 200.
    
    Returns:
        Response: La respuesta obtenida del servidor.
    """
    # Realiza la petición GET.
    response = get(url=url)

    # Comprueba el estado de la respuesta.
    if response.status_code != 200:
        raise NetworkBadResponseError(status_code=response.status_code, reason=HTTPStatus(value=response.status_code).phrase)

    # Retorna la respuesta obtenida.
    return response


def get_html(url:str) -> BeautifulSoup:
    """
    Obtiene el HTMl para una URL dada.

    Args:
        url (str): URl a la que hacer la petición.
    
    Raises:
        NetworkBadResponseError: En caso de que el estado de la petición no sea 200.

    Returns:
        BeautifulSoup: HTML obtenido.
    """
    # Obtiene el HTML.
    response:Response = get_response(url=url)   # Hace la petición GET.
    soup:BeautifulSoup = BeautifulSoup(response.text, "html.parser")

    # Retorna el HTMl obtenido.
    return soup


def url_join(*args) -> str:
    """
    Genera una URL a partir de los argumentos dados.

    Args:
        args: Argumentos a añadir en la URL.
    
    Returns:
        URL: La URL generada.
    """
    # Genera la URL.
    url:str = '/'.join(str(arg).strip('/') for arg in args if arg).strip('/')

    # Devuelve la URL generada.
    return url