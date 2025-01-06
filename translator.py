import time
import os
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

		# Find the drop area
		drop_area = driver.find_element(By.CLASS_NAME, "DBPRyc") # Adjust selector if necessary

		# Find the drag-and-drop area
		# Use JavaScript to simulate drag-and-drop
		file_path = os.path.join(path, os.listdir(path)[0])
		with open(file_path, "rb") as file:
			file_data_base64 = base64.b64encode(file.read()).decode('utf-8')  # Base64-encode and convert to a string

		# Inject JavaScript to simulate a drag-and-drop event
		driver.execute_script("""
			const dropArea = arguments[0];
			const fileData = arguments[1];
			const file = new File([Uint8Array.from(atob(fileData), c => c.charCodeAt(0))], "image.png", { type: "image/png" });
			const dataTransfer = new DataTransfer();
			dataTransfer.items.add(file);
			const dragEvent = new DragEvent("drop", { dataTransfer: dataTransfer });
			dropArea.dispatchEvent(dragEvent);
		""", drop_area, file_data_base64)

		# Optional: Wait to verify upload
		driver.implicitly_wait(10)
