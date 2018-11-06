import falcon
import requests
import configparser

config = configparser.ConfigParser()
config.read('settings.ini')


class Bars:
    def __init__(self):
        self.limit = '10'
        self.client_id = config['FOURSQUARE']['CLIENT_ID']
        self.client_secret = config['FOURSQUARE']['CLIENT_SECRET']
        self.section = 'drinks'
        self.base_url = 'https://api.foursquare.com/v2/venues/explore?'

    def on_get(self, req, resp):
        try:
            self.limit = req.params['limit']
        except KeyError:
            pass

        try:
            self.ll = ','.join(param for param in req.params['ll'])
        except KeyError:
            resp.body = 'Error: param "ll" is not provided'
            resp.status = falcon.HTTP_400
            raise

        url = (self.base_url +
               'client_id=' + self.client_id +
               '&client_secret=' + self.client_secret +
               '&v=20181103&ll=' + str(self.ll) + '&section=' + self.section +
               '&limit=' + self.limit)

        resp.body = requests.get(url).text
        resp.status = falcon.HTTP_200
