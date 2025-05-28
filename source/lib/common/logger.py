# ----------------------------------------------------------------------------------------
# · Filename: logger.py
# · Author: Pablo González García.
# · Copyright (c) 2025 Pablo González García. All rights reserved.
# · Created on: 2025-05-27
# · Descripción: Módulo con funciones encargadas para ayudar con la implementación y 
# configuración de loggers.
# ----------------------------------------------------------------------------------------


# ---- MÓDULOS ---- #
import os

import logging
from logging import Logger, Formatter
from logging import StreamHandler

from lib.config.schema import LoggerConfig


# ---- FUNCIONES ---- #
def create_logger(logger_name:str, logger_config:LoggerConfig=LoggerConfig()):
    """
    Crea y configura un logger. Establece los handlers del logger. Los handlers
    son componentes del logger que permiten mostrar información en diferentes
    salidas como:

        - Consola.
        - Fichero.

    Args:
        logger_name (str): Nombre del logger. Ayuda a identificarlo.
        logger_config (LoggerConfig): Contiene la configuración del logger.

    Raises:
        ValueError: En caso de que alguno de los argumentos sean inválidos o incoherentes.
    
    Returns:
        Logger: Un logger configurado.
    """   
    # Crea el logger base sobre el cual trabajar.
    logger:Logger = Logger(name=logger_name)
    logger.setLevel(getattr(logging, logger_config.level, logging.INFO))     # Establece el nivel mínimo de severidad del logger.

    # Crea el formateador del logger para los mensajes.
    formatter:Formatter = Formatter(fmt=logger_config.format, datefmt=logger_config.dateFmt)

    # Crea el handler de consola.
    consoleHandler:StreamHandler = StreamHandler()
    consoleHandler.setLevel(getattr(logging, logger_config.level, logging.INFO))
    consoleHandler.setFormatter(formatter)
    
    # Añade el handler al logger.
    logger.addHandler(consoleHandler)

    # Retorna el logger configurado.
    return logger