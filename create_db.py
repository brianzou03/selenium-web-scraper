import psycopg2

# Connects to database
connection = psycopg2.connect(
    host='aws-us-east-1-portal.9.dblayer.com',
    port=37393,
    user='admin',
    password='OLHOERSZIIXLIMKQ',
    sslmode='require',
    sslrootcert='C:\\Users\\13236\\PycharmProjects\\seleniumWebScraper\\SSL_Certificate.crt',
    database='compose')

cursor = connection.cursor()

# Drops the table
cursor.execute("""DROP TABLE products """)

# Persists the data to the database
connection.commit()

# Creates a table
cursor.execute("""CREATE TABLE products (id SERIAL PRIMARY KEY,\
name VARCHAR ( 256 ) NOT NULL,\
color VARCHAR (128 ) NOT NULL, \
rating VARCHAR ( 256 ), \
price VARCHAR ( 32 ) NOT NULL,\
link VARCHAR ( 512 ) NOT NULL)""")

connection.commit()
