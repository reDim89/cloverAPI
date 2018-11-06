import falcon

from .addUser import addUser
from .bars import Bars

api = application = falcon.API()

addUser = addUser()
api.add_route('/users', addUser)

bars = Bars()
api.add_route('/bars', bars)
