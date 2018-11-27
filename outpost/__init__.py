import os

import requests
from flask import abort, Flask, send_file, request

from .utils import screenshot


def get_url(url):
    return requests.get(url).content


def validate_url(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url
    return url


def create_app():
    """
    Creates an instance of the Outpost app
    """

    app = Flask(__name__)

    @app.route("/fetch/")
    def fetch_site():
        """
        Standard route for outpost servers. Supports GET requests.
        Request parameter should be keyed as 'url' and
        should include the query url.
        """
        search_url = request.args.get("url")
        if search_url is None:
            abort(400)
        try:
            search_url = validate_url(search_url)
            return get_url(search_url)
        except requests.exceptions.RequestException:
            abort(400)

    @app.route("/screenshot/")
    def fetch_screenshot():
        """
        Standard route for outpost servers. Supports GET requests.
        Request parameter should be keyed as 'url' and
        should include the query url. Returns a screenshot of the url
        """
        search_url = request.args.get("url")
        if search_url is None:
            abort(400)
        search_url = validate_url(search_url)
        img = screenshot.screenshot(search_url, "temp")
        return send_file(os.path.join("..", img))

    @app.route("/")
    def index():
        return "Outpost operational."

    return app
