import falcon

from .api.bars import Bars
from .api.bar_details import Bar_details

api = application = falcon.API()

api.add_route('/bars', Bars())
api.add_route('/bar_details/{id}', Bar_details())
