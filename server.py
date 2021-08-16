import json

import psycopg2
import yaml
from flask import Flask

app = Flask(__name__)


class Server:
    def __init__(self):
        # Opens yaml file and loads configurations
        with open("config.yml", "r") as ymlfile:
            self.cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

        self.connect_db()

    # Connects to database
    def connect_db(self):
        self.connection = psycopg2.connect(
            host=self.cfg["db"]["host"],
            port=self.cfg["db"]["port"],
            user=self.cfg["db"]["user"],
            password=self.cfg["db"]["password"],
            database=self.cfg["db"]["database"],
            sslmode=self.cfg["db"]["sslmode"],
            sslrootcert=self.cfg["db"]["sslrootcert"])

        self.cursor = self.connection.cursor()


# API to fetch by search id
@app.route('/search/<search_id>', methods=['GET'])
# Searches by database key, takes a positive integer
def search(search_id):
    try:
        server.cursor.execute('SELECT * FROM products where id={}'.format(str(search_id)))
        row = server.cursor.fetchone()
        if row is not None:
            return json.dumps(row)
    except TypeError:
        return "The key must be an integer."
    except:
        return "The server encountered an issue."


# API to fetch all records in database
@app.route('/search_all', methods=['GET'])
def search_all():
    try:
        server.cursor.execute('SELECT * FROM products')
        rows = server.cursor.fetchall()
        return json.dumps(rows)
    except:
        return "The server encountered an issue."


if __name__ == '__main__':
    server = Server()
    app.run(host='0.0.0.0', port=8082)
