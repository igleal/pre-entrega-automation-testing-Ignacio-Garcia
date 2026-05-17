import pytest

from utils.helpers import get_chrome_driver, login

@pytest.fixture
def driver():
    driver = get_chrome_driver()
    yield driver
    driver.quit()

@pytest.fixture
def iniciado_sesion(driver):
    login(driver, "standard_user", "secret_sauce")
    return driver