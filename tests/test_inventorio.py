from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_inventario_pagina_carga(iniciado_sesion):
    assert "inventory.html" in iniciado_sesion.current_url

    title = iniciado_sesion.find_element(By.CLASS_NAME, "title").text
    assert title == "Products"

    content = iniciado_sesion.find_element(By.ID, "inventory_container")
    assert content.is_displayed()

def test_inventorio_items_existe(iniciado_sesion):
    items = iniciado_sesion.find_elements(By.CSS_SELECTOR, "[data-test='inventory-item']")
    assert len(items) > 0

    item_nombre = items[0].find_element(By.CLASS_NAME, "inventory_item_name ").text
    assert item_nombre == "Sauce Labs Backpack"

def test_inventorio_carrito_agregar(iniciado_sesion):
    wait = WebDriverWait(iniciado_sesion, 5)

    boton_agregar_item = wait.until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    )
    boton_agregar_item.click()    

    item_verificar_carrito = iniciado_sesion.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert item_verificar_carrito == "1"
    

