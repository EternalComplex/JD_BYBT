import flask, json
from flask import request

server = flask.Flask(__name__)

@server.route("/test", methods=['get'])
def tt():
    return json.dumps({"code": "test"})


if __name__ == "__main__":
    server.run(debug=True, port=8888, host='0.0.0.0')