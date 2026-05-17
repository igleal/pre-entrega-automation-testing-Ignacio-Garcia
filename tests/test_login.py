from utils.helpers import login

from selenium.webdriver.common.by import By

def test_login_saucedemo(driver):
    login(driver, "standard_user", "secret_sauce")

    assert "inventory.html" in driver.current_url

    title = driver.find_element(By.CLASS_NAME, "title").text
    assert title == "Products"

    content = driver.find_element(By.ID, "inventory_container")
    assert content.is_displayed()

