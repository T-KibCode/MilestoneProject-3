import pyscopg2


connection = pyscopg2.connect(database='movie_data')

cursor = connection.cursor()

results = cursor.fetchall()

#results = cursor.fetchone()
connection.close()
for result in results:
    print(result)