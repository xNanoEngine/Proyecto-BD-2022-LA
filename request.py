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
cur.execute("SELECT nombre_medio, count(*) FROM medio_de_prensa m JOIN noticia n ON m.id_medio=n.id_medio GROUP BY nombre_medio")
cur.execute("SELECT nombre_persona")


conn.commit() 
conn.close()