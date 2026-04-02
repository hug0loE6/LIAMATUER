from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
wait = WebDriverWait(driver, 6)
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

for URLexo in listeURLEexo: 
    try:
        driver.get(URLexo)
        #print(f"{URLexo} : I'm starting")
        
        iframe = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe")))
        driver.switch_to.frame(iframe)
        ennonce = driver.find_element(By.CSS_SELECTOR, "body").text #ENNONCE
        driver.switch_to.default_content()

        #la tu fait le print avec ennonce avec l'iaaaaaaa la reponse est stocké dans codeRep
        codeRep = "let bidon: int->int = function x -> x * 2 ;;"

        #La c'est l'input du code
        time.sleep(0.5)
        toutediteur = wait.until(EC.presence_of_element_located((By.ID, "learnocaml-exo-tabs")))
        input = toutediteur.find_element(By.CSS_SELECTOR, "textarea, .ace_text-input")

        #print(f"{URLexo} : I got the input")
        #contenuEditeur = toutediteur.find_elements(By.XPATH, "./*")    
        #zoneCode = contenuEditeur[0].find_elements(By.XPATH, "./*")
        #tabCode = zoneCode[1].find_elements(By.XPATH, "./*")
        #input = tabCode[0]
        input.send_keys(Keys.CONTROL + "a")
        input.send_keys(Keys.BACKSPACE)
        input.send_keys(codeRep)

        #La c'est l'input de graduation
        time.sleep(0.5)
        toolbar = wait.until(EC.presence_of_element_located((By.ID, "learnocaml-exo-toolbar")))
        grade = toolbar.find_element(By.XPATH, ".//button[descendant::span[contains(text(), 'Grade')]]")
        grade.click()
        #a = 0
        #for e in contenuTool :
        #    print(a)
        #    print(e.get_attribute("outerHTML"))
        #    a+=1
        #print(f"{URLexo} : I finished")
        time.sleep(0.5)
        success = False
        try :
            driver.find_element(By.CLASS_NAME, "success")
            success = True
        except :
            success = False
        #print(f"{URLexo} : success = {success}")
        #temporaire juste parce que la je fait 1 fois
    except:
        #print(f"OLOLALALA Y4A UN PB a{URLexo}")
        driver.quit()
driver.quit()