import cv2 
import os 
try: 
    from PIL import Image 
except ImportError: 
    import Image 
import pytesseract

image = cv2.imread('D:\\Users\\lobot\\Desktop\\pyprojects\\macro test\\shield.JPG',0) 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

filename = "{}.jpg".format(os.getpid()) 
cv2.imwrite(filename, gray)

text = pytesseract.image_to_string(Image.open(filename), lang=None) 
os.remove(filename)

print(text) 
cv2.imshow("Image", image) 
cv2.waitKey(0)


