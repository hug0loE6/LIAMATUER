from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)
driver.implicitly_wait(4)
wait = WebDriverWait(driver, 6)
driver.get("https://chat.openai.com")
try :
    time.sleep(5)  # attendre le chargement (à remplacer par WebDriverWait)
    print("locating")
    textarea = wait.until(EC.visibility_of_element_located((By.ID, "prompt-textarea")))
    print("located area")
    actions = ActionChains(driver)
    actions.move_to_element(textarea).click().perform()
    actions.send_keys("Donne un code en python simple").send_keys(Keys.ENTER).perform()

    time.sleep(5) 

    copy_button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Copy code"]')
    copy_button.click()
finally:
    print("ZEGEGGGGGGGGGGGGGGGGGGG")
    #time.sleep(5)
    #driver.quit()
