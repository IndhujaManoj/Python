from PIL import Image
import pytesseract

# Open the exported image from Canva
image = Image.open('coupon.jpeg')  # Replace with the path to your image

# Perform OCR to extract text
extracted_text = pytesseract.image_to_string(image)

# Print the extracted text
print("Extracted Text:")
print(extracted_text)
