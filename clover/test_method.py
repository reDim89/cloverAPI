import json

import falcon


class test_JSON:

    def on_get(self, req, resp):
        json_resp = {
            "firstName": "Иван",
            "lastName": "Иванов",
            "address": {
                   "streetAddress": "Московское ш., 101, кв.101",
                   "city": "Ленинград",
                   "postalCode": "101101"
               },
            "phoneNumbers": [
                   "812 123-1234",
                   "916 123-4567"
            ]
        }

        resp.body = json.dumps(json_resp, ensure_ascii=False)
