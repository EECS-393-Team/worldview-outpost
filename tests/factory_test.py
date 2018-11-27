def get_dfanme_html():
    """
    Helper function that gets test html from my personal website
    """
    f = open("tests/golden/dfan.me.html", "r")
    return f.read()


def test_fetch(client):
    """
    Tests fetch route using my personal website
    """
    response = client.get("/fetch/?url=dfan.me")
    assert response.data.decode("utf-8").replace("\n", "").replace(
        " ", ""
    ) == get_dfanme_html().replace("\n", "").replace(" ", "")


def test_fetch_fail(client):
    """
    Tests fetch route using a bad url
    """
    response = client.get("/fetch/")
    assert response.status_code == 400


def test_screenshot(client):
    """
    Tests screenshot route using my personal website
    """
    response = client.get("/screenshot/?url=dfan.me")
    assert response.data is not None


def test_screenshot_fail(client):
    """
    Tests screenshot route using a bad url
    """
    response = client.get("/screenshot/")
    assert response.status_code == 400
