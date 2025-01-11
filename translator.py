import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.chrome.options as options
import selenium.webdriver.support.ui as ui
import selenium.webdriver.common.by as by
import undetected_chromedriver as uc
import subprocess
import PIL.Image
import time
import os
import io

# Translate to this language
targ_lang = "en"

# Path to the image folder, ending with "/"
# All images in this folder will be deleted at the start of the script and after translating!
image_path = "/home/anilowa/.var/app/org.DolphinEmu.dolphin-emu/data/dolphin-emu/ScreenShots/GAEJ01/"

# Path to the Chrome profile
# Open this profile and press “Accept all” on Google Translate
# Then try pasting an image and always allow clipboard access
# This profile should be in ~/.config/google-chrome
profile_path = "/home/anilowa/.config/google-chrome/Default/"

# Configure Chrome options to allow clipboard access
chrome_options = options.Options()
chrome_options.add_argument(f"--user-data-dir={profile_path}")
chrome_options.add_argument("--profile-directory=Default")

driver = uc.Chrome(options=chrome_options)

# Open the target website
driver.get(f"https://translate.google.com/?sl=auto&tl={targ_lang}&op=images")

# Delete all images in path
for f in os.listdir(image_path):
	os.remove(os.path.join(image_path, f))

first = True

# wait for new files in path
while True:
	if len(os.listdir(image_path)) > 0:
		
		# Images which are not yet fully saved will raise errors:
		
		# PIL.UnidentifiedImageError: cannot identify image file

		# struct.error: unpack_from requires a buffer of at least 4 bytes for unpacking 4 bytes at offset 0 (actual buffer size is 0)
		# followed by:
		# OSError: image file is truncated

		# SyntaxError: broken PNG file

		# Convert image to raw byte data
		byte_io = io.BytesIO()

		try:
			PIL.Image.open(os.path.join(image_path, os.listdir(image_path)[0])).save(byte_io, format='PNG')
		except (PIL.UnidentifiedImageError, OSError, SyntaxError):
			continue

		byte_data = byte_io.getvalue()

		# Use xclip to copy the image to clipboard
		subprocess.Popen(['xclip', '-selection', 'clipboard', '-t', 'image/png'], stdin=subprocess.PIPE).communicate(input=byte_data)

		# Wait for the button to be clickable
		if not first:
			ui.WebDriverWait(driver, 10).until(ec.element_to_be_clickable((by.By.CSS_SELECTOR, "button[aria-label='Clear image']"))).click()

		ui.WebDriverWait(driver, 10).until(ec.element_to_be_clickable((by.By.CSS_SELECTOR, "button[aria-label='Paste an image from clipboard']"))).click()

		# Delete the image
		os.remove(os.path.join(image_path, os.listdir(image_path)[0]))

		time.sleep(1)

		first = False
	
	else:
		time.sleep(1)
