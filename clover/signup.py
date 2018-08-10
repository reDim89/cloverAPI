import psycopg2
import configparser
import falcon

config = configparser.ConfigParser()
config.read('settings.ini')


class Signup:

    def on_get(self, req, resp):

        conn = psycopg2.connect(host=config['DEFAULT']['HOST'],
                                port=config['DEFAULT']['PORT'],
                                user=config['DEFAULT']['USER'],
                                password=config['DEFAULT']['PASSWORD'],
                                dbname=config['DEFAULT']['DBNAME'])

        cur = conn.cursor()

        # cur.execute("INSERT INTO users VALUES (1, 'test', 'test', 'test')")
        cur.execute('SELECT * from users')

        resp.body = cur.fetchall().__str__()
        resp.content_type = falcon.MEDIA_JSON()
        resp.status = falcon.HTTP_200
