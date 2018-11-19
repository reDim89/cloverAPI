import falcon

from .api.bars import Bars

api = application = falcon.API()

api.add_route('/bars', Bars())
