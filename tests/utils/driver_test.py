from outpost.utils import driver


def test_get_driver():
    test_driver, DRIVER = driver.get_driver()
    assert test_driver is not None and DRIVER == "linux" or "mac"
