from decouple import config
import psycopg2

DB_HOST = '127.0.0.1'
DB_NAME = 'test'
DB_USER = 'postgres'
SECRET_KEY = config('pass')

conn = psycopg2.connect(dbname=DB_NAME, user= DB_USER, password = SECRET_KEY, host=DB_HOST)

cur = conn.cursor()

#cur.execute("CREATE TABLE data( FirstName VARCHAR, LastName VARCHAR)")
# cur.execute("ALTER TABLE data ADD id SERIAL PRIMARY KEY;")
# cur.execute("INSERT INTO data( FirstName, LastName) VALUES(%s, %s)", ('Rohit','Singh'))
# cur.execute(" DELETE FROM data WHERE id=4;")

cur.execute("SELECT * FROM data;")
print(cur.fetchall())

conn.commit()

cur.close()
conn.close()