from PIL import Image, ImageDraw, ImageFont

# Define image dimensions and background color
width, height = 800, 400
background_color = (255, 255, 255)

# Create a new image with the specified dimensions and background color
image = Image.new("RGB", (width, height), background_color)

# Create a drawing context
draw = ImageDraw.Draw(image)

# Define fonts and text
font = ImageFont.truetype("arial.ttf", 48)
offer_text = "Limited Time Offer"
details_text = "Get 20% off your next purchase"

# Calculate text positions
offer_x = (width - font.getsize(offer_text)[0]) / 2
offer_y = 50
details_x = (width - font.getsize(details_text)[0]) / 2
details_y = 150

# Define text colors
text_color = (0, 0, 0)

# Draw the text on the image
draw.text((offer_x, offer_y), offer_text, fill=text_color, font=font)
draw.text((details_x, details_y), details_text, fill=text_color, font=font)

# Save the generated offer image
image.save("offer_image.png")

# Show the image (optional)
image.show()
