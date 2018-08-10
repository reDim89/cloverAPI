import falcon

from .signup import Signup

api = application = falcon.API()

signup = Signup()
api.add_route('/signup', signup)
