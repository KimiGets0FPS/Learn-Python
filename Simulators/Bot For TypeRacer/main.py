import selenium
from selenium import webdriver
import seleniumwire
from selenium.webdriver.common.by import By

import os
import sys
from termcolor import cprint
import time
import pynput


driver = webdriver.Chrome()


driver.get("https://www.TypeRacer.com")


