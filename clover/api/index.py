import falcon


class Index:
    def on_get(self, req, resp):
        resp.body = 'Clover API v001'
        resp.status = falcon.HTTP_200
