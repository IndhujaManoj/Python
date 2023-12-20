import pytesseract
from PIL import Image

# Open an image using PIL (Python Imaging Library)
image = Image.open('wallmart.jpg')

# Use pytesseract to extract text from the image
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)
