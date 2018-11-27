import os
from sys import platform

from selenium import webdriver


def get_driver():
    """
    Returns the chromium driver for the current OS
    """

    current_path = os.path.dirname(os.path.abspath(__file__))
    c_path = os.path.join(
        os.path.split(os.path.split(current_path)[0])[0], "chromedriver"
    )
    # Hardcoded path feelsbad
    os.environ["PATH"] = os.environ["PATH"] + ":" + c_path

    if platform.startswith("linux"):
        DRIVER = "linux"
    elif platform == "darwin":
        DRIVER = "mac"
    else:
        raise Exception("Unknown OS")

    return webdriver.Chrome(DRIVER), DRIVER