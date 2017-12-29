"""
Implementation of service A
"""


import flask

from google.appengine.api import users


app = flask.Flask(__name__)


def get_service_b_response():
    """

    :return:
    :rtype: str
    """
    return "nothing"


@app.route("/api/service_a/v1/")
def handler(*args, **kwargs):
    service_b_response = get_service_b_response()
    current_user_nickname = users.get_current_user().nickname()
    response_message = "hello from service A, {}. Service B says \"{}\"".format(
        current_user_nickname,
        service_b_response
    )
    return response_message, 200


if __name__ == '__main__':
    app.run(debug=True)
