from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import sys


if len(sys.argv) != 2:
    print("Respectre la syntaxe suivante : python test.py <token>")
    sys.exit(1)

#token = sys.argv[1]
token = "XST-44Y-PA3-ZX3"

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)
driver.implicitly_wait(4)
listeURLEexo = []

driver.get("http://195.220.87.134/#activity=exercises")
try:
    tokeninput = driver.find_element(By.ID, "login-token-input")
    tokeninput.clear()
    tokeninput.send_keys(token)
    driver.find_element(By.ID, "login-connect-button").click()
except:
    print("Erreur connexion")
    driver.quit()
try:
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
    iframe = driver.find_element(By.CSS_SELECTOR, "iframe")
    driver.switch_to.frame(iframe)
    ennonce = driver.find_element(By.CSS_SELECTOR, "body").text
    driver.switch_to.default_content()
    #la tu fait le print avec ennonce avec l'iaaaaaaa la reponse est stocké dans codeRep

    #La c'est l'input du code
    toutediteur = driver.find_element(By.ID, "learnocaml-exo-tabs")
    contenuEditeur = toutediteur.find_elements(By.XPATH, "./*")    
    zoneCode = contenuEditeur[0].find_elements(By.XPATH, "./*")
    tabCode = zoneCode[1].find_elements(By.XPATH, "./*")
    codeRep = "let bidon: int->int = function x -> x * 2 ;;"
    input = tabCode[0]
    input.send_keys(Keys.CONTROL + "a")
    input.send_keys(Keys.BACKSPACE)
    input.send_keys(codeRep)

    #La c'est l'input de graduation
    toolbar = driver.find_element(By.ID, "learnocaml-exo-toolbar")
    contenuTool = toolbar.find_elements(By.XPATH, "./*")
    contenuTool[5].click()
    
    a = 0
    for e in contenuTool :
        print(a)
        print(e.get_attribute("outerHTML"))
        a+=1

    
finally:
    time.sleep(10)
    driver.quit()
