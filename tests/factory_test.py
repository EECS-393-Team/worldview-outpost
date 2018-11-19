def get_dfanme_html():
    """
    Helper function that gets test html from my personal website
    """
    f = open("tests/dfan.me.html", "r")
    return f.read().strip()


def test_fetch(client):
    """
    Tests fetch route using my personal website
    """
    response = client.get("/fetch/?url=dfan.me")
    assert response.data.decode("utf-8") == get_dfanme_html()


def test_fetch_fail(client):
    """
    Tests fetch route using a bad url
    """
    response = client.get("/fetch/")
    assert response.status_code == 400
