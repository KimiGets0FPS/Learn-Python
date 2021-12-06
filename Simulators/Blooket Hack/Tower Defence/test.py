from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "192.168.0.155")
driver = webdriver.Chrome(options=chrome_options)
print(driver.current_url)

driver.get("https://www.blooket.com")

driver.find_element(By.CLASS_NAME, 'styles__loginButton___3Jo8D-camelCase').click()

