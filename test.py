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
listeURLEexo = []

driver.get("http://195.220.87.134/#activity=exercises")
time.sleep(3)
try:
    tokeninput = driver.find_element(By.ID, "login-token-input")
    tokeninput.clear()
    tokeninput.send_keys(token)
    driver.find_element(By.ID, "login-connect-button").click()
except:
    print("Erreur connexion")
    driver.quit()
try:
    time.sleep(2)
    listeexos = []
    for l in driver.find_elements(By.CSS_SELECTOR, "#learnocaml-main-exercise-list > ul") : 
        listeexos.append(l)
    i = 0
    for l in listeexos : 
        print("section ", i)
        i += 1
        for url in l.find_elements(By.CSS_SELECTOR, "ul li a") :
            listeURLEexo.append(url.get_attribute("href"))
    for url in listeURLEexo :
        print(url)
except:
    print("zebi")
    driver.quit()
#j'ai tout les url la

try:
    driver.get(listeURLEexo[0])
    time.sleep(4)
    iframe = driver.find_element(By.CSS_SELECTOR, "iframe")
    driver.switch_to.frame(iframe)
    ennonce = driver.find_element(By.CSS_SELECTOR, "body").text
    #la tu fait le print avec ennonce avec l'iaaaaaaa la reponse est stocké dans codeRep
    codeRep = "let bidon: int->int = function x -> x * 2 ;;"
    input = driver.find_element(By.CLASS_NAME, "ace_text-input")
    input.send_keys(codeRep)
    
finally:
    time.sleep(5)
    driver.quit()
