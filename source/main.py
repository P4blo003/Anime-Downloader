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


    from lib.core.anime_fenix.anime import AnimeFenixManager
    from lib.core.anime_flv.anime import AnimeFlvManager


    flv = AnimeFlvManager().find_animes("dragon ball")
    fenix = AnimeFenixManager().find_animes("dragon ball")

    print(f"AnimeFlv -> Found: {len(flv)} animes.")
    print(f"- NAME: {flv[0][0]} URL: {flv[0][1]}")
    print(f"AnimeFenix -> Found: {len(fenix)} animes.")
    print(f"- NAME: {fenix[0][0]} URL: {fenix[0][1]}")

    print(AnimeFlvManager().load_anime(flv[0][1]))
    print(AnimeFenixManager().load_anime(fenix[0][1]))