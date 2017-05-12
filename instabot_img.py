#!/usr/bin/env python
"""
instabot_img.py - Instagram Bots for Python
Copyright 2017, KRIPT4

More info:
 * KRIPT4: https://github.com/KRIPT4/Instagram-Bots-for-Python
"""

# Import unittest module for creating unit tests
import unittest

# Import time module to implement 
import time

# Import win32com 
import win32com.client

# Import the Selenium 2 module (aka "webdriver")
from selenium import webdriver

# For automating data input
from selenium.webdriver.common.keys import Keys

# For providing custom configurations for Chrome to run
from selenium.webdriver.chrome.options import Options

varUSER = 'USER@MAIL.COM'
varPASS = 'PASSWORD'
varFILE = 'IMG.jpg'
varTEXT = 'TEXT!'

start_time = time.time()		# TIME EXECUTION TEST

# Select which device you want to emulate by uncommenting it
# More information at: https://sites.google.com/a/chromium.org/chromedriver/mobile-emulation
mobile_emulation = { 
	#"deviceName": "Apple iPhone 3GS"
	#"deviceName": "Apple iPhone 4"
	#"deviceName": "Apple iPhone 5"
	#"deviceName": "Apple iPhone 6"
	#"deviceName": "Apple iPhone 6 Plus"
	#"deviceName": "BlackBerry Z10"
	#"deviceName": "BlackBerry Z30"
	#"deviceName": "Google Nexus 4"
	"deviceName": "Google Nexus 5"
	#"deviceName": "Google Nexus S"
	#"deviceName": "HTC Evo, Touch HD, Desire HD, Desire"
	#"deviceName": "HTC One X, EVO LTE"
	#"deviceName": "HTC Sensation, Evo 3D"
	#"deviceName": "LG Optimus 2X, Optimus 3D, Optimus Black"
	#"deviceName": "LG Optimus G"
	#"deviceName": "LG Optimus LTE, Optimus 4X HD" 
	#"deviceName": "LG Optimus One"
	#"deviceName": "Motorola Defy, Droid, Droid X, Milestone"
	#"deviceName": "Motorola Droid 3, Droid 4, Droid Razr, Atrix 4G, Atrix 2"
	#"deviceName": "Motorola Droid Razr HD"
	#"deviceName": "Nokia C5, C6, C7, N97, N8, X7"
	#"deviceName": "Nokia Lumia 7X0, Lumia 8XX, Lumia 900, N800, N810, N900"
	#"deviceName": "Samsung Galaxy Note 3"
	#"deviceName": "Samsung Galaxy Note II"
	#"deviceName": "Samsung Galaxy Note"
	#"deviceName": "Samsung Galaxy S III, Galaxy Nexus"
	#"deviceName": "Samsung Galaxy S, S II, W"
	#"deviceName": "Samsung Galaxy S4"
	#"deviceName": "Sony Xperia S, Ion"
	#"deviceName": "Sony Xperia Sola, U"
	#"deviceName": "Sony Xperia Z, Z1"
	#"deviceName": "Amazon Kindle Fire HDX 7″"
	#"deviceName": "Amazon Kindle Fire HDX 8.9″"
	#"deviceName": "Amazon Kindle Fire (First Generation)"
	#"deviceName": "Apple iPad 1 / 2 / iPad Mini"
	#"deviceName": "Apple iPad 3 / 4"
	#"deviceName": "BlackBerry PlayBook"
	#"deviceName": "Google Nexus 10"
	#"deviceName": "Google Nexus 7 2"
	#"deviceName": "Google Nexus 7"
	#"deviceName": "Motorola Xoom, Xyboard"
	#"deviceName": "Samsung Galaxy Tab 7.7, 8.9, 10.1"
	#"deviceName": "Samsung Galaxy Tab"
	#"deviceName": "Notebook with touch"
			
# Or specify a specific build using the following two arguments
#"deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
#"userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" }
}

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