#!/usr/bin/env python
"""
instabot_img.py - Instagram Bots for Python
Copyright 2017, KRIPT4

More info:
 * KRIPT4: https://github.com/KRIPT4/Instagram-Bots-for-Python
"""

import time
import win32com.client
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

varUSER = 'USER@MAIL.COM'
varPASS = 'PASSWORD'
varFILE = 'IMG.jpg'
varTEXT = 'TEXT!'

start_time = time.time()		# TIME EXECUTION TEST

mobile_emulation = {
    "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" }
chrome_options = Options()
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--allow-running-insecure-content')
chrome_options.add_argument('--disable-web-security')
chrome_options.add_argument('--no-referrers')
chrome_options.add_argument('--window-size=375,773')
chrome_options.add_experimental_option('prefs', {
    'credentials_enable_service': False,
    'profile': {
        'password_manager_enabled': False
    }
})
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(chrome_options = chrome_options)
driver.get('https://www.instagram.com/')
time.sleep(4)

## LOGIN
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div[2]/p/a').click()
time.sleep(1)
driver.find_element_by_name('username').send_keys(varUSER)
driver.find_element_by_name('password').send_keys(varPASS)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div[1]/div/form/span/button').click()
time.sleep(3)
## END LOGIN

## UPLOAD FILE
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div/div/div[2]/div/div/div[3]/div').click()
time.sleep(2)
## OPEN FILE DIALOG
shell = win32com.client.Dispatch("WScript.Shell")   
shell.Sendkeys(varFILE)  
shell.Sendkeys("~")
## END OPEN FILE DIALOG
time.sleep(2)
driver.find_element_by_xpath('//*[@id="react-root"]/div/div[1]/header/div[2]/button').click()
driver.find_element_by_xpath('//*[@id="react-root"]/div/div[2]/section/div/textarea').clear()
driver.find_element_by_xpath('//*[@id="react-root"]/div/div[2]/section/div/textarea').send_keys('varTEXT')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="react-root"]/div/div[1]/header/div[2]/button').click()
time.sleep(5)
## END UPLOAD FILE

driver.quit()

elapsed_time = time.time() - start_time
print("Elapsed time: %.10f seconds." % elapsed_time)