import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_cadastroUsuario():
    navegador = webdriver.Chrome()

    try:
        navegador.maximize_window()

        navegador.get("https://www.amazon.com.br/ref=nav_logo")

        wait = WebDriverWait(navegador, 10)
        campo_busca = wait.until(
            EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
        )
        campo_busca.send_keys("Caneca")
        
        # Faz a busca
        realiza_busca = navegador.find_element(
            By.ID,
            "nav-search-submit-button"
        )
        realiza_busca.click()
        
        time.sleep(5)

        adicionarFiltroMarca = navegador.find_element(
            By.XPATH,
            "/html/body/div[1]/div[1]/div[1]/div[2]/div/div[3]/span/div[1]/span/div/div[3]/div[3]/ul/span/span[1]/li/span/a/div"
        )
        adicionarFiltroMarca.click()

        time.sleep(5)

        clica_primeiroItem = wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR,
                "[data-asin='B07V3GPBKJ'] a[href*='/dp/']"
            ))
        )
        clica_primeiroItem.click()
        
        time.sleep(3)
        
    finally:
        navegador.quit()