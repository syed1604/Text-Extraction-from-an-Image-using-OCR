#import the libraries
import pytesseract
import pkg_resources
import cv2

from PIL import Image
import pytesseract
import cv2
#declaring the exe path for tesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def ocr(file):

    #loading the image from the disk
    image_to_ocr = cv2.imread(file)
    #preprocessing the image
    # step 1 : covert to grey scale
    preprocessed_img = cv2.cvtColor(image_to_ocr, cv2.COLOR_BGR2GRAY)
    # step 2 : Do binary and otsu thresholding
    preprocessed_img = cv2.threshold(preprocessed_img,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    # step 3 : Smooth the image using median blur
    preprocessed_img = cv2.medianBlur(preprocessed_img, 3)
    #save the preprocessed image temporarily into the disk
    cv2.imwrite('temp_img.jpg',preprocessed_img)
    #read the temp image from disk as pil image
    preprocessed_pil_img = Image.open('temp_img.jpg')
    #pass the pil image to tesseract to do OCR
    text_extracted = pytesseract.image_to_string(preprocessed_pil_img)
    return text_extracted
