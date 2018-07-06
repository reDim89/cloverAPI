import falcon

from .test_method import test_JSON

api = application = falcon.API()

test_JSON = test_JSON()
api.add_route('/test_JSON', test_JSON)
