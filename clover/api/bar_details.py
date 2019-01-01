import falcon
from ..controller import bars_controller


class Bar_details:
    def __init__(self):
        self._controller = bars_controller.Bars_controller()

    def on_get(self, req, resp, id):
        resp.body = self._controller.get_venue_details(id=id)
        resp.status = falcon.HTTP_200
