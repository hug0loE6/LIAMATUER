from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
import time

options = webdriver.FirefoxOptions()
options.set_preference("intl.accept_languages", "en-US,en")
driver = webdriver.Firefox(options=options)
wait = WebDriverWait(driver, 15)

try:
    driver.get("https://gemini.google.com")
    aa = "Il s'agit d'écrire la définition OCaml de la fonction bidon, qui étant donné un entier, calcule son double."
    cookie = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Accept all"]')))
    cookie.click()
    prompt_box = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".ql-editor")))
    prompt_box.click()
    ennonce = f"""Pour ta réponse au prompt, je veux seulement un bloc de code, et pas de contenu a coté.
    "Prompt : En ocaml faire l'exo suivant :
    {aa}"""
    prompt_box.send_keys(ennonce)
    prompt_box.send_keys(Keys.ENTER)

    copy_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Copy code"]')))
    copy_button.click()
    code = pyperclip.paste()
    print(code)
finally:
    time.sleep(50)
    driver.quit()
