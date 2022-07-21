import falcon
from wsgiref.simple_server import make_server


class Healthz:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_TEXT
        resp.text = "healthy"


app = falcon.App()
app.add_route("/healthz", Healthz())
with make_server("", 6502, app) as api:
    print("Running on 0.0.0.0:6502")
    api.serve_forever()
