import selenium
from selenium import webdriver
import seleniumwire
from selenium.webdriver.common.by import By

import os
import sys
from termcolor import cprint
import time
import pyautogui


print("-----------------------------\nInstalling some necessary packages...\n-----------------------------")
time.sleep(2)

os.system("py -m pip install --upgrade pip")
os.system("py -m pip install selenium")
os.system("py -m pip install selenium-wire")

os.system("py -m pip install termcolor")


time.sleep(1)
cprint("\nDone!", color="blue")
time.sleep(2)

sys.stdout.flush()

driver = webdriver.Chrome()

# url = driver.command_executor._url
# session_id = driver.session_id

# driver = webdriver.Remote(command_executor=url, desired_capabilities={})
# driver.close()   # this prevents the dummy browser
# driver.session_id = session_id


# # driver.find_element_by_class_name("")


# options = webdriver.ChromeOptions()
# options.add_experimental_option('debuggerAddress', 'localhost:9014')
# driver = webdriver.Chrome(options=options)

driver.get("https://www.blooket.com")

driver.find_element(By.CLASS_NAME, 'styles__loginButton___3Jo8D-camelCase').click()

fin = open("questions_answers.txt", 'r')

question_sets = {}
num_q = int(fin.readline())

for i in range(num_q):
    sets = fin.readline().split(':')
    question_sets = {sets[0]: ''.join(sets[1].split())}

time.sleep(5)

# driver.close()
