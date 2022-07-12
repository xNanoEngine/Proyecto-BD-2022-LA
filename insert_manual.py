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

cur.execute("USE region_LosRios")
cur.execute("INSERT INTO autor VALUES ('1','NONE')")
cur.execute("INSERT INTO dueno VALUES ('1','NONE', 'financiación privada', 'DESCONOCIDO')")
cur.execute("INSERT INTO medio_de_prensa VALUES ('1','1', 'RED LOS RIOS', '10-01-01', 'Espanol', 'Los rios', 'https://redlosrios.com/', 'Chile')")
cur.execute("INSERT INTO noticia VALUES ('1','1','1','https://redlosrios.com/policial/corte-de-valdivia-ordena-vacunar-a-recien-nacida-luego-que-padres-se', 'CORTE DE VALDIVIA ORDENA VACUNAR A RECIÉN NACIDA LUEGO QUE PADRES SE NEGARAN ADUCIENDO MOTIVOS RELIGIOSOS', '22-07-8', 'La Corte de Apelaciones de Valdivia acogió el recurso de protección presentado por el Hospital Base de Osorno, en contra de los padres de una recién nacida que, por razones religiosas, se niegan a inocular a su hija con la vacuna obligatoria BCG que protege contra la tuberculosis en todas sus variantes y la vacuna HBV, que protege de la infección crónica con el virus de la hepatitis, las que están incluidas en el plan nacional de inmunización del Ministerio de Salud.')")
cur.execute("INSERT INTO persona VALUES ('1','1', 'Desconocido','Doctor','Carlos Eduardo Currieco Pavié', '0', 'Chileno')")

conn.commit() 
conn.close()