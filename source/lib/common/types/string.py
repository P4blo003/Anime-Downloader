# ----------------------------------------------------------------------------------------
# · Filename: string.py
# · Author: Pablo González García.
# · Copyright (c) 2025 Pablo González García. All rights reserved.
# · Created on: 2025-05-28
# · Descripción: Módulo con funciones encargadas para procesar cadenas.
# ----------------------------------------------------------------------------------------


# ---- FUNCIONES ---- #
def clear_str(value:str) -> str:
    """
    Limpia la cadena dada de espacios antes y después de la cadena, así como
    de exceso de espacios.

    Args:
        value (str): La cadena a formatear.
    
    Returns:
        str: Cadena formateada.
    """
    # Procesa la cadena.
    value = value.strip("")             # Limpia espacios antes y despues de la cadena.
    value.replace("\r", "")             # Elimina carácteres.
    value.replace("\n", "")             # Elimina carácteres.
    value = ' '.join(value.split())     # Elimina exceso de espacios.

    # Retorna la cadena formateada.
    return value