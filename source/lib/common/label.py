# ----------------------------------------------------------------------------------------
# · Filename: label.py
# · Author: Pablo González García.
# · Copyright (c) 2025 Pablo González García. All rights reserved.
# · Created on: 2025-05-27
# · Descripción: Módulo con funciones encargadas para mostrar mensajes, títulos, etc.,
# por consola.
# ----------------------------------------------------------------------------------------


# ---- MÓDULOS ---- #
from typing import List
from shutil import get_terminal_size


# ---- FUNCIONES ---- #
def print_header(title:str) -> any:
    """
    Imprime la cabecera del programa.

    Args:
        title (str): Título a imprimir.
    """
    # Preprocesa el texto.
    title = title.strip()

    # Obtiene el número de columnas de la consola.
    columns:int = get_terminal_size().columns
    left_space:int = int((columns - len(title)) / 2)

    # Imprime la cabeceras.
    print(f"{'='*columns}")
    print(f"{' '*left_space}{title}")
    print(f"{'='*columns}")


def print_actions(header:str, actions:List[str]) -> any:
    """
    Imprime el listado de acciones.

    Args:
        header (str): Cabecera de las acciones.
        actions List[str]: Lista con las acciones a imprimir.
    """
    # Imprime las acciones.
    print(f"{'-'*5} {header} {'-'*5}")
    for index, action in enumerate(actions):
        print(f"{index}) {action}")