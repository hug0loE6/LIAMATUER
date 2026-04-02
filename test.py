from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import InvalidArgumentException
import time
import pyperclip
import subprocess
import sys


if len(sys.argv) != 2:
    print("Respectre la syntaxe suivante : python test.py <token>")
    sys.exit(1)

#token = sys.argv[1]
token = "XST-44Y-PA3-ZX3"

options = webdriver.FirefoxOptions()
options.set_preference("intl.accept_languages", "en-US,en")
try :
    driver = webdriver.Firefox(options=options)
except InvalidArgumentException as e :
    print(e)
    result = subprocess.run(
    ["snap", "info", "firefox"],
    capture_output=True,
    text=True)
    options.binary_location = result.stdout
    driver = webdriver.Firefox(options=options)
driver.implicitly_wait(4)
waitsympa = WebDriverWait(driver, 6)
waitgiminicegroslard = WebDriverWait(driver, 60)
listeURLEexo = []

driver.get("http://195.220.87.134/#activity=exercises")
driver.execute_script("window.open('https://gemini.google.com');")
tabs = driver.window_handles
#gemini into accept cookie into casse toi
driver.switch_to.window(tabs[1])
cookie = waitsympa.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Accept all"]')))
cookie.click()
driver.close()
driver.switch_to.window(tabs[0])
time.sleep(0.5)
try:
    tokeninput = waitsympa.until(EC.presence_of_element_located((By.ID, "login-token-input")))
    tokeninput.clear()
    tokeninput.send_keys(token)
    driver.find_element(By.ID, "login-connect-button").click()
except:
    print("Erreur connexion")
    driver.quit()
    exit()
try:
    listeexos = []
    for l in waitsympa.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#learnocaml-main-exercise-list > ul"))) : 
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
    exit()
#j'ai tout les url la

for URLexo in listeURLEexo: 
    try:
        driver.get(URLexo)
        #print(f"{URLexo} : I'm starting")
        
        iframe = waitsympa.until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe")))
        driver.switch_to.frame(iframe)
        ennonce = driver.find_element(By.CSS_SELECTOR, "body").text #ENNONCE
        driver.switch_to.default_content()

        driver.execute_script("window.open('https://gemini.google.com');")
        tabs = driver.window_handles
        driver.switch_to.window(tabs[1])
        ennonce = f"""Pour ta réponse au prompt, je veux seulement un bloc de code, et pas de contenu a coté.
        "Prompt : En ocaml faire l'exo suivant :
        {ennonce}"""
        prompt_box = waitsympa.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".ql-editor")))
        prompt_box.click()
        prompt_box.send_keys(ennonce)
        prompt_box.send_keys(Keys.ENTER)
        copy_button = waitgiminicegroslard.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Copy code"]')))
        copy_button.click()
        codeRep = pyperclip.paste()
        driver.close()
        driver.switch_to.window(tabs[0])
        #La c'est l'input du code
        time.sleep(0.5)
        toutediteur = waitsympa.until(EC.presence_of_element_located((By.ID, "learnocaml-exo-tabs")))
        input = toutediteur.find_element(By.CSS_SELECTOR, "textarea, .ace_text-input")

        input.send_keys(Keys.CONTROL + "a")
        input.send_keys(Keys.BACKSPACE)
        input.send_keys(codeRep)

        #La c'est l'input de graduation
        time.sleep(0.5)
        toolbar = waitsympa.until(EC.presence_of_element_located((By.ID, "learnocaml-exo-toolbar")))
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
        print(f"{URLexo} : success = {success}")
    except:
        print(f"OLOLALALA Y4A UN PB a{URLexo}")
        driver.quit()

driver.quit()