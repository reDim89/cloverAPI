import psycopg2
import configparser
import falcon
import json

config = configparser.ConfigParser()
config.read('settings.ini')


class addUser:

    def on_post(self, req, resp):
        body = req.stream.read(req.content_length or 0)
        bd = json.loads(body.decode('utf-8'))

        conn = psycopg2.connect(host=config['DEFAULT']['HOST'],
                                port=config['DEFAULT']['PORT'],
                                user=config['DEFAULT']['USER'],
                                password=config['DEFAULT']['PASSWORD'],
                                dbname=config['DEFAULT']['DBNAME'])

        cur = conn.cursor()

        cur.execute('INSERT INTO users' +
                    '(nickname, first_name, last_name)' +
                    'VALUES (%s, %s, %s)',
                    (bd['nickname'], bd['first_name'], bd['last_name']))

        conn.commit()

        cur.close()
        conn.close()

        resp.body = 'Success!'
        resp.content_type = falcon.MEDIA_JSON
        resp.status = falcon.HTTP_200

    def on_get(self, req, resp):
        resp.body = 'Success!'
        resp.status = falcon.HTTP_200
