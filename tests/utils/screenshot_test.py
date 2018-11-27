import os

from outpost.utils import screenshot
from PIL import Image


def import_golden():
    """
    Helper method which imports the example screenshot
    """
    return Image.open("tests/golden/dfan.me.png")


def test_screenshot():
    """
    Tests the screenshot method
    """
    ss = screenshot.screenshot("http://dfan.me", "temp")
    assert os.path.exists(ss)
