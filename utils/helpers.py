from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

""" Tuve problemas con el webdriver_manager que me descargaba una version vieja en mi pc (114) cuando tenia la (148), asi que buscando manera de solucionar (borrando cache, actualizando, etc.) no me funcionaba, hasta que encontre que selenium desde hace un tiempo para aca tiene ahora su propio manejador de driver, el cual si me funcionaba asi que ese es el que estoy utilizando aqui"""

def get_chrome_driver():
    # service = Service(ChromeDriverManager().install())
    # driver = webdriver.Chrome(service=service)

    driver = webdriver.Chrome()

    return driver

def login(driver, username, password):
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.saucedemo.com/")

    username_element = wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    
    username_element.send_keys(username)

    password_element = wait.until(
        EC.visibility_of_element_located((By.ID, "password"))
    )

    password_element.send_keys(password)

    button_element = wait.until(
        EC.element_to_be_clickable((By.ID, "login-button"))
    )

    button_element.click()