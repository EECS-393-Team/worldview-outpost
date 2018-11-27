import os

from . import driver


def screenshot(url, out):
    """
    Returns a screenshot of the given url in a dummy chrome browser
    """

    webdriver, _ = driver.get_driver()
    webdriver.get(url)
    screenshot = os.path.join(out, "screenshot.png")
    if not webdriver.save_screenshot(screenshot):
        raise Exception("Screenshot Failed")
    webdriver.quit()
    return screenshot
