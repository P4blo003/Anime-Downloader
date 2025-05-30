# ----------------------------------------------------------------------------------------
# · Filename: int.py
# · Author: Pablo González García.
# · Copyright (c) 2025 Pablo González García. All rights reserved.
# · Created on: 2025-05-28
# · Descripción: Módulo con funciones encargadas para procesar enteros.
# ----------------------------------------------------------------------------------------


# ---- FUNCIONES ---- #
def int_to_str(num:int, result_length:int) -> str:
    """
    Convierte el entero dado a una cadena. La transformación consiste en añadir
    0 a la izquierda del número dado en función del valor de `result_length`.

        - Dado `num = 12` y `result_length = 3` el resultado es `012`.
    
    Args:
        num (int): El número a transformar.
        result_length (int): La longitud del resultado.

    Returns:
        str: El número formateado en una cadena.
    """
    # Convierte el número a cadena.
    strFmt:str = str(num)

    # Comprueba la longitud de la cadena.
    if len(strFmt) > result_length:
        #TODO: Excepción.
        pass

    # Añade 0 a la izquierda del número hasta completar los ceros.
    diff:int = result_length - len(strFmt)      # Obtiene el resto hasta la longitud final.
    result:str = f"{'0'*diff}{strFmt}"          # Genera la cadena.

    # Devuelve el resultado.
    return result