
import pytesseract
from pytesseract import Outpute
from PIL import Image
import cv2

img_path1 = '/Users/kevin/Desktop/Screenshot 2024-02-07 at 11.28.28 AM.png'
text = pytesseract.image_to_string(img_path1,lang='eng')
print(text)     

img_path2 = '/Users/kevin/Desktop/Screenshot 2024-02-08 at 2.59.13 PM.png'

print(pytesseract.image_to_data(img_path1))