"""
    FICHIER GÉRANT LA CONFIGURATION POUR LA LIAISON DU SERVER POSTGRESQL
"""
import os
import psycopg2
from dotenv import load_dotenv

# CHARGER LE FICHIER ENV
load_dotenv()

# ACCEDER AUX VARIABLES DU FICHIER ENV
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_SCHEMA = os.getenv("DB_SCHEMA")

def se_connecter():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD 
    )




