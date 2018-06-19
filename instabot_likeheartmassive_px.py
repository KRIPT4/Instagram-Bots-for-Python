#!/usr/bin/env python
"""
@name: instabot_likeheartmassive_px.py - Instagram Bots for Python (Proxy Version)
@disclaimer: Copyright 2017, KRIPT4
@lastrelease: Mon May 15 2017 17:49:42
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
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import *
from selenium.webdriver.chrome.options import Options

NewProxy = "PROXYIPADDRESS:PORT"

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
chrome_options.add_argument('--proxy-server=%s' % NewProxy)
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
	driver  = webdriver.Chrome(executable_path = '?:\PATH\TO\chromedriver.exe', chrome_options = chrome_options)
	varUSER = 'USERNAME'
	varPASS = 'PASSWORD'

	start_time = time.time()		# TIME EXECUTION TEST
	time.sleep(2)
	driver.get('https://www.instagram.com/accounts/login/')
	time.sleep(1)

	## LOGIN
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	retryElement('//*[@name = "username"]').send_keys(varUSER)
	retryElement('//*[@name = "password"]').send_keys(varPASS)
	retryElement('//*[@id="react-root"]/section/main/article/div/div/div/form/span/button').click()

	## SAVE LOGIN SESION
	retryElement('//*[@id="react-root"]/section/main/div/section/div/span/button').click()
	## END SAVE LOGIN SESION

	time.sleep(2)
	driver.execute_script('divsToHide=document.getElementsByClassName("_bfc7q");divsToHide[0].style.display="none";')
	time.sleep(2)
	## END LOGIN

	for i in range(1, 11): # For loop from 1 to 10
		try:
			valueact = '//*[@id="react-root"]/section/main/section/div/div[1]/article[' + str(i) + ']/div[2]/section[1]/a[1]'
			valuehea = '//*[@id="react-root"]/section/main/section/div/div[1]/article[' + str(i) + ']/div[2]/section[1]/a[1]/span'
			WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, valueact)))
			ulike = retryElement(valuehea).get_attribute("class")
			if ulike == '_soakw coreSpriteLikeHeartOpen':
				retryElement(valueact).click()
				print("Instagram LikeHeart N°:", i)
				driver.execute_script('elements=document.getElementsByClassName("coreSpriteLikeHeartOpen");elements[0].parentNode.scrollIntoView();')
				time.sleep(1)
			else:
				print("Instagram Already like N°:", i)
		except:
			print("Instagram LikeHeart Error!", i) 

	driver.quit()
	elapsed_time = time.time() - start_time
	print("Elapsed time: %.1f seconds." % elapsed_time)

def retryElement(xpath):
	for i in range(0,50):
		try:
			element = driver.find_element_by_xpath(xpath)
			return element
		except Exception as e:
			time.sleep(0.1)
			continue
	brikear(("Error xpath: %s" % xpath))

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