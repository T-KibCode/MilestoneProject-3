import psycopg2

# connect to the database
connnection = psycopg2.connect(database="movies.session.sql")

# build a cursor object of the database
cursor = connnection.cursor()


#query 1 select all records from the movies table
cursor.execute("SELECT * FROM movies")

#fetch the result (all)
results = cursor.fetchall("SELECT * FROM movies")

# fetch the result (single)
# result = cursor.fetchone()

# close the connection
connnection.close()

# print the result
for result in results:
    print(result)

