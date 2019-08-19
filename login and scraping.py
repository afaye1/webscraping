from selenium import webdriver
import os
import time
from bs4 import BeautifulSoup
import requests

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")

def bot(passwd, usrnm):
    br = webdriver.Chrome(executable_path = DRIVER_BIN)
    br.get("<website_login_URL>")
    
    username = br.find_element_by_id('username')
    password = br.find_element_by_id('pwd')
    #check page source for elements
    btn = br.find_element_by_class_name('login-form-submit')

    username.send_keys('')
    password.send_keys()
    btn.click()
    
    br.get("<website_url>")
    
    something = br.find_element_by_id("<id>")
    something.click()
    time.sleep(3)
    somethingelse = br.find_element_by_xpath("<id>")
    somethingelse.click()
    anothersomething = br.find_element_by_xpath('<id>')
    anothersomething.click()
    time.sleep(1)
    download = br.find_element_by_xpath('<id>')
    download.click()


if __name__ == "__main__":
    
    file = open("<name_your_file>.txt", 'r')    
    info = file.readlines()
    file.close()
    bot(info[0], info[1])