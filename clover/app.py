import falcon

from .addUser import addUser

api = application = falcon.API()

addUser = addUser()
api.add_route('/users', addUser)
