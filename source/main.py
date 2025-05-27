# ----------------------------------------------------------------------------------------
# · Filename: main.py
# · Author: Pablo González García.
# · Copyright (c) 2025 Pablo González García. All rights reserved.
# · Created on: 2025-05-07
# · Descripción: Módulo que contiene la lógica principal del programa.
# ----------------------------------------------------------------------------------------


# ---- MÓDULO ---- #
from logging import Logger
from lib.common.logger import create_logger


# ---- LÓGICA PRINCIPAL ---- #
if __name__ == "__main__":

    # -- Variables globales -- #
    logger:Logger = create_logger(logger_name=__name__)

    # -- Flujo principal -- #
    logger.info("Iniciada ejecición del programa.")