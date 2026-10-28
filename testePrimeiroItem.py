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

        clica_primeiroItem = navegador.find_element(
            By.XPATH,
            "/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div"
        )
        clica_primeiroItem.click()
        
    finally:
        navegador.quit()