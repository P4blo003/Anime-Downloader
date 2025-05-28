# ----------------------------------------------------------------------------------------
# · Filename: main.py
# · Author: Pablo González García.
# · Copyright (c) 2025 Pablo González García. All rights reserved.
# · Created on: 2025-05-07
# · Descripción: Módulo que contiene la lógica principal del programa.
# ----------------------------------------------------------------------------------------


# ---- MÓDULOS ---- #
from lib.common.label import print_header, print_actions


# ---- LÓGICA PRINCIPAL ---- #
if __name__ == "__main__":

    # -- Flujo principal -- #
    print_header("Anime-Downloader")            # Imprime el título.

    print_actions(header='Acciones', actions=['Listar Animes', 'Buscar Animes'])