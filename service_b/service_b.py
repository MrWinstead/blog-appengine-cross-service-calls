"""
Implementation of service B
"""


import flask


app = flask.Flask(__name__)


@app.route("/api/service_b/v1/")
def handler(*args, **kwargs):
    return "Hello from Service B", 200


if __name__ == '__main__':
    app.run(debug=True)
