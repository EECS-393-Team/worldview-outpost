import requests
from flask import abort, Flask, request


def get_url(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url
    return requests.get(url).content


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
            return get_url(search_url)
        except requests.exceptions.RequestException:
            abort(400)

    @app.route("/")
    def index():
        return "Outpost operational."

    return app
