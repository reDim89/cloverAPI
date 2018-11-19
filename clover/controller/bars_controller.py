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
        self._base_url = 'https://api.foursquare.com/v2/venues/explore?'
        self._version = '20181103'

    def _get_bars(self, limit, ll):

        payload = {'client_id': self._client_id,
                   'client_secret': self._client_secret,
                   'v': self._version,
                   'll': str(ll),
                   'section': self._section,
                   'limit': limit
                   }

        self._response = requests.get(self._base_url, params=payload)
        return self._response.status_code

    def _extract_bar_data(self, limit, ll):

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
            items_list = self._extract_bar_data(limit, ll)
        except RuntimeError:
            return None

        for item in items_list:
            d = {'id': item['venue']['id'],
                 'name': item['venue']['name'],
                 'address': item['venue']['location']['address'],
                 'lat': item['venue']['location']['lat'],
                 'lng': item['venue']['location']['lng']}
            venues_list.append(OrderedDict(sorted(d.items())))

        return json.dumps(venues_list, ensure_ascii=False)


if __name__ == '__main__':

    bars = Bars_controller()
    print(bars.get_venues(limit=10, ll='55.730149,37.61556'))
