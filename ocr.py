import pytesseract
from PIL import Image

def extract_text(image_path):
    # Open the image and extract text using Tesseract OCR
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

