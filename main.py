import random
from wsgiref.simple_server import make_server

import falcon


class Healthz:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_TEXT
        resp.text = "healthy"


class Info:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_JSON
        resp.media = {
            "apiversion": "1",
            "author": "CP",
            "color": "#FF00FF",
            "head": "bender",
            "tail": "sharp",
        }


class Move:
    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_JSON
        move = random.choice(["up", "down", "left", "right"])
        resp.media = {"move": move}
        print(req.media)


class Start:
    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_TEXT
        resp.text = "ok"
        print(req.media)


class End:
    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_TEXT
        resp.text = "ok"
        print(req.media)


if __name__ == "__main__":
    app = falcon.App()
    app.add_route("/", Info())
    app.add_route("/move", Move())
    app.add_route("/start", Start())
    app.add_route("/end", End())
    app.add_route("/healthz", Healthz())
    with make_server("", 6502, app) as api:
        print("Running on 0.0.0.0:6502")
        api.serve_forever()
