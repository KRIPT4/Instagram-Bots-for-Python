#!/usr/bin/env python
"""
@name: instabot_imgmassive.py - Instagram Bots for Python
@disclaimer: Copyright 2017, KRIPT4
@lastrelease: Sat May 13 2017 14:28:10
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
global lstFiles

def mainExe():
	global lstFiles
	global driver
	driver  = webdriver.Chrome(executable_path = '?:\PATH\TO\chromedriver.exe', chrome_options = chrome_options)
	varUSER = 'USERNAME'
	varPASS = 'PASSWORD'
	varTEXT = 'TESTPOST'

	start_time = time.time()		# TIME EXECUTION TEST
	
	filelisting()
	time.sleep(2)

	driver.get('https://www.instagram.com/accounts/login/')
	time.sleep(1)

	## LOGIN
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	retryElement('//*[@name = "username"]').send_keys(varUSER)
	retryElement('//*[@name = "password"]').send_keys(varPASS)
	retryElement('//*[@id="react-root"]/section/main/article/div/div/div/form/span/button').click()
	## END LOGIN

	## SAVE LOGIN SESION
	retryElement('//*[@id="react-root"]/section/main/div/section/div/span/button').click()
	## END SAVE LOGIN SESION

	for elemento in lstFiles:

		## UPLOAD FILE
		retryElement('//*[@id="react-root"]/section/nav/div/div/div[2]/div/div/div[3]/div').click()
		## OPEN FILE DIALOG
		shell = win32com.client.Dispatch("WScript.Shell")
		time.sleep(3) #<-- falta control aca
		shell.Sendkeys(elemento)  
		shell.Sendkeys("~")
		## END OPEN FILE DIALOG
		retryElement('//*[@id="react-root"]/div/div[1]/header/div[2]/button').click()
		retryElement('//textarea[@class="_8od8r"]').clear()
		retryElement('//textarea[@class="_8od8r"]').send_keys(varTEXT)
		retryElement('//*[@id="react-root"]/div/div[1]/header/div[2]/button').click()
		time.sleep(5)
		## END UPLOAD FILE

	driver.quit()

	elapsed_time = time.time() - start_time
	print("Elapsed time: %.1f seconds." % elapsed_time)

def filelisting():
	global lstFiles
	#Variable for path to directory
	path = '/DOWNLOADS/IMAGES'

	#List empty to include files
	lstFiles = []
	 
	#List with all files in the directory:
	lstDir = os.walk(path)
 
	#Creates a list of the image (JPG/JPEG/PNG) files that exist in that directory.
	for root, dirs, files in lstDir:
		for fichero in files:
			(nombreFichero, extension) = os.path.splitext(fichero)
			if(extension == ".jpg"):
				lstFiles.append(nombreFichero+extension)
			if(extension == ".jpeg"):
				lstFiles.append(nombreFichero+extension)
			if(extension == ".png"):
				lstFiles.append(nombreFichero+extension)
			if(extension == ".gif"):
				lstFiles.append(nombreFichero+extension)

	print(lstFiles)

def retryElement(xpath):
	for i in range(0,50):
		try:
			element = driver.find_element_by_xpath(xpath)
			return element
		except Exception as e:
			time.sleep(0.1)
			continue
	brikear(("no se encontro elemento xpath: %s" % xpath))

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