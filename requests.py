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
cur.execute("SELECT nombre, count(*) FROM medio_de_prensa m JOIN noticia n ON m.id_medio=n.id_medio GROUP BY nombre")
print("a.")
for row in cur:
    print(row)
cur.execute("SELECT nombre_persona, fecha_publicacion FROM noticia m JOIN persona n ON m.id_noticia=n.id_noticia")
print("b.")
for row in cur:
    print(row)
cur.execute("SELECT nombre_persona, cantidad FROM persona m JOIN popularidad n ON m.id_persona=n.id_persona HAVING nombre_persona='Carlos Eduardo Currieco Pavié'")
print("c.")
for row in cur:
    print(row)
cur.execute("SELECT nombre, fecha_creacion FROM medio_de_prensa m ORDER BY fecha_creacion DESC LIMIT 5")
print("d.")
for row in cur:
    print(row)
conn.commit() 
conn.close()