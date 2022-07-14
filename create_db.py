import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="root",
        host="127.0.0.1",
        port=3306
    )

except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

# Create Database
query_create = "CREATE DATABASE region_LosRios"
cur.execute(query_create)
cur.execute("USE region_LosRios")
cur.execute("CREATE TABLE dueno (id_dueno INT AUTO_INCREMENT PRIMARY KEY, nombre_dueno VARCHAR(300), tipo_dueno VARCHAR(300), fecha_adquisicion DATE)")
cur.execute("CREATE TABLE autor (id_autor INT AUTO_INCREMENT PRIMARY KEY, nombre_autor VARCHAR(300))")
cur.execute("CREATE TABLE medio_de_prensa (id_medio INT AUTO_INCREMENT PRIMARY KEY,id_dueno INT, FOREIGN KEY (id_dueno) REFERENCES dueno(id_dueno), nombre VARCHAR(300), fecha_creacion DATE, url_media VARCHAR(300), region VARCHAR(300), pais VARCHAR(300), idioma VARCHAR(300))")
cur.execute("CREATE TABLE noticia (id_noticia INT AUTO_INCREMENT PRIMARY KEY, id_autor INT ,FOREIGN KEY (id_autor) REFERENCES autor(id_autor), id_medio INT ,FOREIGN KEY (id_medio) REFERENCES medio_de_prensa(id_medio), url VARCHAR(300), titulo VARCHAR(300), fecha_publicacion DATE, contenido TEXT)")
cur.execute("CREATE TABLE persona (id_persona INT AUTO_INCREMENT PRIMARY KEY, id_noticia INT, FOREIGN KEY (id_noticia) REFERENCES noticia(id_noticia), nombre_persona VARCHAR(300), nacionalidad VARCHAR(300), popularidad INT, profesion VARCHAR(300), fecha_nacimiento VARCHAR(300))")

conn.commit() 
conn.close()