import PIL.ImageGrab
import pytesseract
import googletrans
import PIL

# Main monitor (original text)
main_x = 1920
main_y = 1080

# Secondary monitor (output text)
sec_x = 1600
sec_y = 900

# Is main monitor on the right?
mainRight = True

"""
Only works for two monitor layouts
Main monitor can't be shorter than secondary and secondary monitor has to be contained within main monitor's height

Examples:

......MMMMMMMMMMMMMM
SSSSSSMMMMMMMMMMMMMM
SSSSSSMMMMMMMMMMMMMM
SSSSSSMMMMMMMMMMMMMM
mainRight = True

MMMMSSSSSS
MMMMSSSSSS
MMMMSSSSSS
mainRight = False

Other configurations are not supported
"""

PIL.ImageGrab.grab((sec_x, 0, sec_x + main_x, main_y) if mainRight else (0, 0, main_x, main_y)).show()