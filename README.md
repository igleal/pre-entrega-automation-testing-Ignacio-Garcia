# Proyecto de Automatización con Selenium - SauceDemo

## Propósito del proyecto

Este proyecto tiene como objetivo aplicar los conocimientos adquiridos, automatizando flujos básicos de navegación web utilizando **Selenium WebDriver** y **Python**.

La automatización está enfocada en el sitio de práctica **SauceDemo** (`www.saucedemo.com`), una aplicación diseñada para testing, donde se validan funcionalidades como el inicio de sesión, la visualización del inventario y la interacción con el carrito de compras.

---

## Tecnologías utilizadas

- Python → Lenguaje principal del proyecto  
- Pytest → Framework de testing  
- Selenium WebDriver → Automatización de navegador  
- Git / GitHub → Control de versiones  

---

## Estructura del proyecto

```bash
proyecto/
│
├── test/
│   ├── test_login.py
│   └── test_inventario.py
│
├── utils/
│   └── helpers.py
│
├── conftest.py
├── README.md
├── reporte.html
├── requirements.txt
```

---

## Instalación de proyecto

### 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_PROYECTO>
```

### 2. Instalar dependencias

pip install -r requirements.txt

## Cómo ejecutar las pruebas

### Ejecutar todas las pruebas

pytest -v

### Ejecutar pruebas específicas

pytest test/test_login.py -v
pytest test/test_inventario.py -v
