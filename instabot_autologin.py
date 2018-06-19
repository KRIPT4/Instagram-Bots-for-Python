#!/usr/bin/env python
"""
@name:instabot_img_px.py - Instagram Bots for Python (Proxy Version)
@disclaimer:Copyright 2017, KRIPT4
@lastrelease: Mon May 15 2017 18:01:27
More info:
 * KRIPT4: https://github.com/KRIPT4/Instagram-Bots-for-Python
"""

import os
import sys

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

start_time = time.time()		# TIME EXECUTION TEST

# Select which device you want to emulate by uncommenting it
# More information at: https://sites.google.com/a/chromium.org/chromedriver/mobile-emulation
mobile_emulation = { "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 }, "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" }
chrome_options = Options()
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--allow-running-insecure-content')
chrome_options.add_argument('--enable-precise-memory-info')
chrome_options.add_argument('--ignore-ssl-errors=true --debug=true')
chrome_options.add_argument('--window-size=375,773')
chrome_options.add_experimental_option('prefs', {
    'credentials_enable_service': False,
    'profile': {
        'password_manager_enabled': False
    }
})
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
global driver

def mainExe():
	global driver
	varUSER = 'USERNAME'
	varPASS = 'PASSWORD'
	driver = webdriver.Chrome(executable_path = '?:\PATH\TO\chromedriver.exe', chrome_options = chrome_options)
	driver.get('https://www.instagram.com/accounts/login/')
	time.sleep(1)

	## LOGIN
	retryElement('//*[@name = "username"]').send_keys(varUSER)
	retryElement('//*[@name = "password"]').send_keys(varPASS)
	retryElement('//*[@id="react-root"]/section/main/article/div/div/div/form/span/button').click()
	## END LOGIN

	## SAVE LOGIN SESION
	retryElement('//*[@id="react-root"]/section/main/div/section/div/span/button').click()
	## END SAVE LOGIN SESION

	driver.quit()

	elapsed_time = time.time() - start_time
	print("Elapsed time: %.10f seconds." % elapsed_time)

def retryElement(xpath):
	for i in range(0,100):
		try:
			element = driver.find_element_by_xpath(xpath)
			return element
		except Exception as e:
			time.sleep(0.1)
			continue
	brikear(("Error XPATH: %s" % xpath))

def brikear(msg):
	print(msg)
	closeDriver()
	sys.exit(1)

def closeDriver():
	global driver
	driver.quit()

try:
	mainExe()
except Exception as e:
	print(e)
	closeDriver()