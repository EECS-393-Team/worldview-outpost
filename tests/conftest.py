import pytest

from outpost import create_app


@pytest.fixture
def app():
    """
    PyTest fixture to yield an app instance.
    """
    app = create_app()
    yield app


@pytest.fixture
def client(app):
    """
    Returns an app fixture for testing.
    """
    return app.test_client()
