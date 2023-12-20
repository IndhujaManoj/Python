from PIL import Image, ImageDraw, ImageFont
import qrcode
# Create a blank image with a white background
width, height = 1000, 2000  # You can use your desired resolution
image = Image.new("RGB", (width, height), "rgb(18,75,69)")
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=5,
    border=4,
)
qr.add_data('https://www.google.com')
qr.make(fit=True)
qr_image = qr.make_image(fill_color='black', back_color='white')

image.paste(qr_image, (width - 100, height - 100))

# Create a drawing context
draw = ImageDraw.Draw(image)

# Use a specific TrueType font for better quality
font = ImageFont.truetype("./fonts/Montserrat,Roboto/Roboto/Roboto-Italic.ttf", size=70)  # Provide the path to a TrueType font
font_size = 72

# Define the text and position
text = "Sundar Retails"
text_position = (50, 50)

# Set the text color
text_color = (0, 0, 0)  # Black

# Add the text to the image
draw.text(text_position, text, fill=text_color, font=font)

# Save the image as a high-quality JPEG with compression quality (1-95)
image.save("./text_image.jpg", "JPEG", quality=100)

