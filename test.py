from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import sys


if len(sys.argv) != 2:
    print("Respectre la syntaxe suivante : python test.py <token>")
    sys.exit(1)

token = sys.argv[1]
driver = webdriver.Chrome()

driver.get("http://195.220.87.134/#activity=exercises")
time.sleep(4)
try:
    tokeninput = driver.find_element(By.ID, "login-token-input")
    tokeninput.clear()
    tokeninput.send_keys(token)
    driver.find_element(By.ID, "login-connect-button").click()
except:
    print("Erreur connexion")
    driver.quit()
try:
    time.sleep(4)
    listeexos = []
    for l in driver.find_elements(By.CSS_SELECTOR, "#learnocaml-main-exercise-list ul li") : 
        listeexos.append(l)
    
except:
    print("zebi")
    driver.quit()

