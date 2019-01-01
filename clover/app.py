import falcon

from .api.bars import Bars
from .api.bar_details import Bar_details
from .api.index import Index

api = application = falcon.API()

api.add_route('/bars', Bars())
api.add_route('/bar_details/{id}', Bar_details())
api.add_route('/', Index())
