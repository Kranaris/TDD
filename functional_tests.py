from selenium import webdriver
from selenium.webdriver.chrome.service import Service

options = webdriver.FirefoxOptions()
options.add_argument("-headless")

browser = webdriver.Firefox(options=options)
browser.get('http://127.0.0.1:8000')

assert 'The install worked successfully! Congratulations!' in browser.title
