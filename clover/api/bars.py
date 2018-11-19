import falcon
from ..controller import bars_controller


class Bars:
    def __init__(self):
        self._controller = bars_controller.Bars_controller()

    def on_get(self, req, resp):
        lim = req.params['limit']
        latlng = ','.join(l for l in req.params['ll'])

        resp.body = self._controller.get_venues(limit=lim,
                                                ll=latlng)
        resp.status = falcon.HTTP_200
