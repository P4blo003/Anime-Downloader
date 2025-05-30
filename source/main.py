# ----------------------------------------------------------------------------------------
# · Filename: main.py
# · Author: Pablo González García.
# · Copyright (c) 2025 Pablo González García. All rights reserved.
# · Created on: 2025-05-07
# · Descripción: Módulo que contiene la lógica principal del programa.
# ----------------------------------------------------------------------------------------


# ---- MÓDULOS ---- #
from lib.common.label import print_header


# ---- LÓGICA PRINCIPAL ---- #
if __name__ == "__main__":

    # -- Flujo principal -- #
    print_header("Anime-Downloader")            # Imprime el título.

    from lib.core.animeFlv import AnimeFlv

    m = AnimeFlv()

    animes = m.find_anime("Sword Art Online")

    from lib.core.animeFlv import AnimeFlv_Anime
    
    url = animes[0][1]

    anime:AnimeFlv_Anime = AnimeFlv_Anime(url=url)

    print(anime)