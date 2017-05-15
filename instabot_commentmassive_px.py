#!/usr/bin/env python
"""
@name: instabot_commentmassive_px.py - Instagram Bots for Python (Proxy Version)
@disclaimer: Copyright 2017, KRIPT4
@lastrelease: Mon May 15 2017 18:30:32
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
mobile_emulation = { "deviceName": "Google Nexus 5"}
chrome_options = Options()
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--allow-running-insecure-content')
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
	driver  = webdriver.Chrome(executable_path = 'chromedriver.exe', chrome_options = chrome_options)
	varUSER = 'USERNAME'
	varPASS = 'PASSWORD'
	varTEXT = 'COMMENT!'

	start_time = time.time()		# TIME EXECUTION TEST
	time.sleep(2)
	driver.get('https://www.instagram.com/')
	time.sleep(1)

	## LOGIN
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	retryElement('//*[@id="react-root"]/section/main/article/div/div[2]/p/a').click()
	retryElement('//*[@name = "username"]').send_keys(varUSER)
	retryElement('//*[@name = "password"]').send_keys(varPASS)
	retryElement('//*[@id="react-root"]/section/main/article/div/div[1]/div/form/span/button').click()
	time.sleep(2)
	driver.execute_script('divsToHide=document.getElementsByClassName("_bfc7q");divsToHide[0].style.display="none";')
	time.sleep(2)
	## END LOGIN

	for i in range(1, 11): # For loop from 1 to 10
		try:
			time.sleep(15)
			valueact = '//*[@id="react-root"]/section/main/section/div/div[1]/article[' + str(i) + ']/div[2]/section[3]/form/input'
			valuebtc = '//*[@id="react-root"]/section/main/section/div/div[1]/article[' + str(i) + ']/div[2]/section[3]/form/button'
			WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, valueact)))
			retryElement(valueact).send_keys(varTEXT)
			retryElement(valuebtc).click()
			print("Instagram Comment N°:", i)
			driver.execute_script('function getElementByXpath(path) {return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;}elements=document.getElementByXpath(' + valueact + ');elements[0].parentNode.scrollIntoView();')
		except:
			print("Instagram Comment Error!", i) 

	#driver.quit()
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