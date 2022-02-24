import psycopg2
from dotenv import load_dotenv
from os import environ

load_dotenv()
user = environ["USUARIO"]
password = environ["PASSWORD"]
host = environ["HOST"]
port = int(environ["PORT"])
db = environ["DB"]

def conexion(func):
    def with_conexion(*args, **kwargs):
        # with psycopg2.connect("postgresql://andyjair:maga@localhost/andyjair") as conn:
        with psycopg2.connect(user=user, password=password, dbname=db) as conn:
            cur = conn.cursor()
            datos = func(cur, *args, **kwargs)
        return datos
    return with_conexion
