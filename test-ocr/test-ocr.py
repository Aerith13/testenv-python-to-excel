import pytesseract
from PIL import Image

# Path to the Tesseract executable 
pytesseract.pytesseract.tesseract_cmd = r'c:/Program Files/Tesseract-OCR/tesseract.exe'

# Function to extract text from an image using Tesseract OCR
def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

# Test the script with a sample image
image_path = 'c:/Users/Aretex/Desktop/tst4.png'
extracted_text = extract_text_from_image(image_path)
print(extracted_text)