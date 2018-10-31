from flask import Flask

app = Flask(__name__)


@app.route("/fetch")
def fetch_site():
    return "Fetching Site"
