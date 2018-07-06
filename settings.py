# Based on https://habrahabr.ru/post/276731/

# Database URI
# read here how to get it: http://docs.mlab.com/connecting/#connect-string

MONG_URI = "mongodb://admin:admin@ds217898.mlab.com:17898/clover"

# Supported methods
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

# Format output as JSON
RENDERERS = ['eve.render.JSONRenderer']

# Database login credentials
MONGO_HOST = 'ds217898.mlab.com',
MONGO_PORT = 17898
MONGO_USERNAME = 'admin'
MONGO_PASSWORD = 'admin'
MONGO_DBNAME = 'clover'

# Database config
# Use following cURL command to add items, while running on local machine
'''
curl -i  \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{"username": "reDim89", "firstname": "Dima", "lastname": "Taranov"}' \
  http://localhost:5000/users
'''

DOMAIN = {
    'users': {
              'schema':
             {
                      'firstname': {
                          'type': 'string',
                          'minlength': 1,
                          'maxlength': 10,
                      },
                      'lastname': {
                          'type': 'string',
                          'minlength': 1,
                          'maxlength': 15,
                          'required': True
                      },
                      'username': {
                          'type': 'string',
                          'minlength': 5,
                          'maxlength': 32,
                          'required': True,
                          'unique': True
                      }
                  }
           }
}
