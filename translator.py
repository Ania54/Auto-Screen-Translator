import time
import os
import io
import subprocess
import PIL.Image
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import selenium
from selenium.webdriver.chrome.options import Options

# Configure Chrome options to allow clipboard access
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.clipboard": 1}) # 1 = Allow
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)

# Path to your Chrome user data directory
# chrome_options = Options()
# chrome_options.add_argument("--user-data-dir=/home/anilowa/.config/google-chrome/Default")

# Launch browser with your existing profile
driver = webdriver.Chrome(options=chrome_options)

# Open the target website
driver.get("https://translate.google.com/?sl=auto&tl=en&op=images")

# Path to the image folder, ending with "/"
# All images in this folder will be deleted at the start of the script and after translating
path = "/home/anilowa/.var/app/org.DolphinEmu.dolphin-emu/data/dolphin-emu/ScreenShots/GAEJ01/"

# Delete all images in path
# for f in os.listdir(path):
# 	os.remove(os.path.join(path, f))

# wait for new files in path
while True:
	if len(os.listdir(path)) > 0:
		# get first file in path
		# show the image
		time.sleep(.1)

		# Open the image using Pillow
		image = PIL.Image.open(os.path.join(path, os.listdir(path)[0])) #os.listdir(path)[0])

		# Convert image to raw byte data
		byte_io = io.BytesIO()
		image.save(byte_io, format='PNG')
		byte_data = byte_io.getvalue()

		# Use xclip to copy the image to clipboard
		process = subprocess.Popen(
			['xclip', '-selection', 'clipboard', '-t', 'image/png'],
			stdin=subprocess.PIPE)

		process.communicate(input=byte_data)
		
		# Wait for the button to be clickable
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Accept all']"))).click()

		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Paste an image from clipboard']"))).click()

		input()
	
	else:
		time.sleep(1)
