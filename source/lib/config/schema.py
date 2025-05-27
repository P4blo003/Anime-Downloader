# ----------------------------------------------------------------------------------------
# · Filename: schema.py
# · Author: Pablo González García.
# · Copyright (c) 2025 Pablo González García. All rights reserved.
# · Created on: 2025-05-07
# · Descripción: Módulo con las clases encargadas de almacenar las
# configuraciones de los diversos componentes.
# ----------------------------------------------------------------------------------------


# ---- MÓDULOS ---- #
from pydantic import BaseModel
from pydantic import Field


# ---- CLASES ---- #
class LoggerConfig(BaseModel):
    """
    Almacena la configuración relacionada con el Logger del programa.

    Attributes:
        level (str): Nivel mínimo de severidad del logger.
        format (str): El formato de los mensajes del log.
        dateFmt (str): Formato de la fecha del mensaje del log.
        maxBytes (int): Tamaño máximo en bytes del fichero log.
        backupCount (int): Controla cuántos archivos de respaldo se conservan al hacer rotación
            de logs.
    """
    # -- Atributos -- #
    level:str       = Field(default="INFO", pattern="DEBUG|INFO|WARNING|ERROR|CRITICAL")
    format:str      = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    dateFmt:str     = '%Y-%m-%d %H:%M:%S'
    maxBytes:int    = 10 * 1024 * 1024  # 10 MB.
    backupCount:int = 5