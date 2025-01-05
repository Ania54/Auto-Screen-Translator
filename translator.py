import PIL.ImageEnhance
import PIL.ImageGrab
import pytesseract
import googletrans
import PIL.Image
import PIL
import cv2

# Source language
src_lang = "jpn"

# Main monitor (original text)
main_x = 1920
main_y = 1080

# Secondary monitor (output text)
sec_x = 1600
sec_y = 900

# Is main monitor on the right?
mainRight = True

"""
* Only works for two monitor layouts
* Main monitor can't be shorter than the secondary one
* Secondary monitor has to be contained within main monitor's height

Examples:

......MMMMMMMMMMMMMM
SSSSSSMMMMMMMMMMMMMM
SSSSSSMMMMMMMMMMMMMM
SSSSSSMMMMMMMMMMMMMM
(mainRight = True)

MMMMSSSSSSSS
MMMMSSSSSSSS
MMMMSSSSSSSS
(mainRight = False)

Other configurations are not supported
"""

screen = PIL.ImageGrab.grab((sec_x, 0, sec_x + main_x, main_y) if mainRight else (0, 0, main_x, main_y))
screen = PIL.ImageEnhance.Contrast(PIL.Image.open("test.png").convert("L")).enhance(2)

print(pytesseract.image_to_string(screen, lang=src_lang))