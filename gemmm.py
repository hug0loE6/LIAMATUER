from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    # 1. Aller sur Gemini (Attention : demande une connexion Google en réel)
    driver.get("https://gemini.google.com")
    time.sleep(50)  # Attendre que la page charge (ajuster si nécessaire)

    # 2. Attendre que l'élément soit présent et cliquable
    # On utilise un Sélecteur CSS pour la classe 'ql-editor'
    wait = WebDriverWait(driver, 10)
    prompt_box = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".ql-editor")))

    # 3. Cliquer pour donner le focus (important sur les div éditables)
    prompt_box.click()

    # 4. Taper le texte
    prompt_box.send_keys("Bonjour Gemini, comment vas-tu ?")

    # 5. Appuyer sur Entrée
    prompt_box.send_keys(Keys.ENTER)

    # Laisser le temps de voir la réponse commencer
    time.sleep(5)

finally:
    driver.quit()