import psycopg2

db = psycopg2.connect("news")
c = db.cursor()
c.execute("...")
c.fetchall()
db.close()
db.commit()
