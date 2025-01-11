from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import subprocess
import PIL.Image
import time
import os
import io

# Translate to this language
targ_lang = "en"

# Path to the image folder, ending with "/"
# All images in this folder will be deleted at the start of the script and after translating
path = "/home/anilowa/.var/app/org.DolphinEmu.dolphin-emu/data/dolphin-emu/ScreenShots/GAEJ01/"

# Configure Chrome options to allow clipboard access
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.clipboard": 1}) # 1 = Allow
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)

# Path to your Chrome user data directory
# chrome_options = Options()
# chrome_options.add_argument("--user-data-dir=/home/anilowa/.config/google-chrome/Default")

# Launch browser with your existing profile
# driver = webdriver.Chrome(options=chrome_options)
driver = uc.Chrome()

# Remove navigator.webdriver property
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
	"source": """
		Object.defineProperty(navigator, 'webdriver', {
			get: () => undefined
		})
	"""
})

# Open the target website
driver.get(f"https://translate.google.com/?sl=auto&tl={targ_lang}&op=images")

# Delete all images in path
# for f in os.listdir(path):
# 	os.remove(os.path.join(path, f))

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Accept all']"))).click()

first = True

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
		if not first:
			WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Clear image']"))).click()

		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Paste an image from clipboard']"))).click()

		# Delete the image
		os.remove(os.path.join(path, os.listdir(path)[0]))

		first = False
	
	else:
		time.sleep(1)
