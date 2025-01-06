import PIL.ImageEnhance
import PIL.ImageGrab
import pytesseract
import googletrans
import PIL.Image
import cv2

# Source language (OCR)
src_lang = "jpn+eng"

"""

bbox = (x1, y1, x2, y2)
P(x1, y1) is the upper left corner, and Q(x2, y2) is the lower right corner
These are coordinates of all screens in a layout

So on a dual monitor setup, the points P and Q would be here:

P       1111111111111111
        1111111111111111
222222221111111111111111
222222221111111111111111
222222221111111111111111
22222222               Q

"""

bbox = (1600, 0, 3520, 1080)

screen = PIL.ImageGrab.grab(bbox).save("test.png")

# to do: downscale (divide by 2)

# PIL.ImageEnhance.Contrast(PIL.Image.open("test.png").convert("L")).enhance(2).save("test_e.png")

cv2.imwrite("test_c.png", cv2.threshold(cv2.imread("test.png", cv2.IMREAD_GRAYSCALE), 127, 255, cv2.THRESH_BINARY)[1])

print(pytesseract.image_to_string(PIL.Image.open("test_c.png"), lang=src_lang))