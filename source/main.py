# ----------------------------------------------------------------------------------------
# · Filename: main.py
# · Author: Pablo González García.
# · Copyright (c) 2025 Pablo González García. All rights reserved.
# · Created on: 2025-05-07
# · Descripción: Módulo que contiene la lógica principal del programa.
# ----------------------------------------------------------------------------------------


# ---- MÓDULOS ---- #
from lib.common.label import print_header, print_actions

from lib.core.animeFlv import AnimeFlv


# ---- LÓGICA PRINCIPAL ---- #
if __name__ == "__main__":

    # -- Flujo principal -- #
    print_header("Anime-Downloader")            # Imprime el título.

    mng = AnimeFlv()

    animes = mng.find_anime("DraGon  baLl   2")

    anime = animes[0]

    anime.load_episodes()

    anime.Episodes[0].load_download_servers()

    print(anime.Episodes[0].DownloadServers)