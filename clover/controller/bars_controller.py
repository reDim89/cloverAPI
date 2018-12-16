import requests
import configparser
import json

from collections import OrderedDict

config = configparser.ConfigParser()
config.read('settings.ini')


class Bars_controller:
    def __init__(self):
        self._client_id = config['FOURSQUARE']['CLIENT_ID']
        self._client_secret = config['FOURSQUARE']['CLIENT_SECRET']
        self._section = 'drinks'
        self._base_url = 'https://api.foursquare.com/v2/venues/'
        self._version = '20181103'

    def _get_bars(self, limit, ll):

        payload = {'client_id': self._client_id,
                   'client_secret': self._client_secret,
                   'v': self._version,
                   'll': str(ll),
                   'section': self._section,
                   'limit': limit
                   }

        self._response = requests.get(self._base_url + 'explore',
                                      params=payload)
        return self._response.status_code

    def _extract_bars_list(self, limit, ll):

        self._get_bars(limit, ll)

        try:
            items_list = [item for item in self._response.json()
                          ['response']
                          ['groups']
                          [0]
                          ['items']]
        except KeyError:
            print('Items are missing in API repsose')
            return None

        return items_list

    def get_venues(self, limit, ll):
        venues_list = []
        try:
            items_list = self._extract_bars_list(limit, ll)
        except RuntimeError:
            return None

        for item in items_list:
            try:
                d = {'id': item['venue']['id'],
                     'name': item['venue']['name'],
                     'address': item['venue']['location']['address'],
                     'lat': item['venue']['location']['lat'],
                     'lng': item['venue']['location']['lng']}
            except KeyError:
                d = {'id': item['venue']['id'],
                     'name': item['venue']['name'],
                     'lat': item['venue']['location']['lat'],
                     'lng': item['venue']['location']['lng']}
            venues_list.append(OrderedDict(sorted(d.items())))

        return json.dumps(venues_list, ensure_ascii=False)

    def get_venue_details(self, id):
        payload = {'client_id': self._client_id,
                   'client_secret': self._client_secret,
                   'v': self._version,
                   }

        self._response = requests.get(self._base_url + id,
                                      params=payload).json()['response']

        photo_url = (self._response['venue']['bestPhoto']['prefix'] +
                     str(self._response['venue']['bestPhoto']['width']) + 'x' +
                     str(self._response['venue']['bestPhoto']['height']) +
                     self._response['venue']['bestPhoto']['suffix'])

        venue_details = {'name': self._response['venue']['name'],
                         # 'description':self._response['venue']['description']
                         'price': self._response['venue']['price']['tier'],
                         'photo': photo_url,
                         'url': self._response['venue']['url']
                         }

        return json.dumps(venue_details, ensure_ascii=False)
