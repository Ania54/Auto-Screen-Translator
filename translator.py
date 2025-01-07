import time
import os
import io
import base64
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# Set up the WebDriver (use the correct driver for your browser)
driver = webdriver.Firefox()

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

		time.sleep(10)
                
		# Open the image using Pillow
    		image = Image.open(image_path)

    		# Convert image to raw byte data
    		byte_io = io.BytesIO()
    		image.save(byte_io, format='PNG')
    		byte_data = byte_io.getvalue()

    		# Use xclip to copy the image to clipboard
    		process = subprocess.Popen(
        		['xclip', '-selection', 'clipboard', '-t', 'image/png'],
        		stdin=subprocess.PIPE
    		)
    		process.communicate(input=byte_data)

		# Optional: Wait to verify upload
		driver.implicitly_wait(10)
