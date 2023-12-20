from PIL import Image, ImageFont, ImageDraw
import qrcode

# Create a blank image with a custom background color
width, height = 1000, 2000
background_color = (222, 214, 216)  # Custom background color (light gray)
image = Image.new("RGB", (width, height), background_color)

# Create a QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=5,
    border=4,
)
qr.add_data('https://www.google.com')
qr.make(fit=True)
qr_image = qr.make_image(fill_color='black', back_color='white')

# Calculate the position to center the QR code
qr_x = (width - qr_image.width) // 2
qr_y = (height - qr_image.height) // 2

# Paste the QR code in the center of the image
image.paste(qr_image, (qr_x, qr_y))

# Use a specific TrueType font for better quality
font_path_title = "./fonts/Montserrat,Roboto/Montserrat/static/Montserrat-Black.ttf"
# Normal text font
font_path_t2_t3 = "./fonts/Montserrat,Roboto/Roboto/Roboto-Italic.ttf"

font_path_t4 = "./fonts/Montserrat,Roboto/Roboto/Roboto-Bold.ttf"
font_size = 70
font = ImageFont.truetype(font_path_title, size=font_size)
normal_font_size = 40
normal_font = ImageFont.truetype(font_path_t2_t3, size=normal_font_size)

# Define the main text
text = "Sundar Retails."
text2 = "You trusted health partner for"
text3 = "pharmaceutical needs and expert care"
offerBox = "Rs 200 OFF"

# Set the text color to white
text_color = (255, 255, 255)  # White

# Define text4 and its font size
text4 = "• coupon valid up to 24 Oct, 2023 •"
text4_font_size = 50

# Create a round-bordered rectangle with rounded corners using a mask
border_radius = 30  # Increase the radius to make the corners more rounded
rect_width = width - 20
rect_height = 750  # Adjust the height as needed
rect_color = (18, 75, 69)  # RGB color for the round rectangle
draw = ImageDraw.Draw(image)

# Create a mask for the round-bordered rectangle
mask = Image.new("L", (rect_width, rect_height), 0)
mask_draw = ImageDraw.Draw(mask)
mask_draw.rectangle([(border_radius, border_radius), (rect_width - border_radius, rect_height - border_radius)],
                   fill=255)
mask_draw.ellipse((0, 0, 2 * border_radius, 2 * border_radius), fill=0)
mask_draw.ellipse((rect_width - 2 * border_radius, 0, rect_width, 2 * border_radius), fill=0)
mask_draw.ellipse((0, rect_height - 2 * border_radius, 2 * border_radius, rect_height), fill=0)
mask_draw.ellipse((rect_width - 2 * border_radius, rect_height - 2 * border_radius, rect_width, rect_height),
                   fill=0)

# Paste the round-bordered rectangle onto the image
image.paste(rect_color, (10, 10), mask)

# Add text1 inside the round-bordered rectangle
text_mask = font.getmask(text)
text_x = (width - text_mask.getbbox()[2]) // 2
text_y = 70  # Adjust the y coordinate to center the text vertically
draw.text((text_x, text_y), text, fill=text_color, font=font)

# Adjust the spacing between text1 and text2
spacing = 50  # Adjust the spacing as needed

# Add text2 inside the round-bordered rectangle
text2_mask = normal_font.getmask(text2)
text2_x = (width - text2_mask.getbbox()[2]) // 2
text2_y = text_y + text_mask.getbbox()[3] + spacing  # Adjust the y coordinate with spacing
draw.text((text2_x, text2_y), text2, fill=text_color, font=normal_font)

# Adjust the spacing between text2 and text3
spacing = 15  # Adjust the spacing as needed

# Add text3 inside the round-bordered rectangle
text3_mask = normal_font.getmask(text3)
text3_x = (width - text3_mask.getbbox()[2]) // 2
text3_y = text2_y + text2_mask.getbbox()[3] + spacing  # Adjust the y coordinate with spacing
draw.text((text3_x, text3_y), text3, fill=text_color, font=normal_font)

# Adjust the spacing between text3 and text4
spacing = 50  # Increase the spacing as needed

# Load the font with the specified size for text4
text4_font = ImageFont.truetype(font_path_t4, size=text4_font_size)

# Calculate the position for text4 and adjust the y-coordinate
text4_mask = text4_font.getmask(text4)
text4_x = (width - text4_mask.getbbox()[2]) // 2
text4_y = text3_y + text3_mask.getbbox()[3] + spacing  # Adjust the y-coordinate with increased spacing

# Add text4 inside the round-bordered rectangle with the adjusted font size
draw.text((text4_x, text4_y), text4, fill=text_color, font=text4_font)

# Create a rectangle for the offer box
offer_box_width = 300
offer_box_height = 100
offer_box_x = (width - offer_box_width) // 2
offer_box_y = text4_y + text4_font_size + 50  # Adjust the vertical position below text4
offer_box_color = (255, 249, 219)  # RGB color for the offer box
draw.rectangle([offer_box_x, offer_box_y, offer_box_x + offer_box_width, offer_box_y + offer_box_height], fill=offer_box_color)

# Add text to the offer box
offer_box_font_size = 40
offer_box_font = ImageFont.truetype(font_path_title, size=offer_box_font_size)
offer_box_text = "Rs 200 OFF"
offer_box_text_mask = offer_box_font.getmask(offer_box_text)
offer_box_text_x = (offer_box_width - offer_box_text_mask.getbbox()[2]) // 2 + offer_box_x
offer_box_text_y = offer_box_y + (offer_box_height - offer_box_text_mask.getbbox()[3]) // 2
offer_box_text_color = (0, 0, 0)
draw.text((offer_box_text_x, offer_box_text_y), offer_box_text, fill=offer_box_text_color, font=offer_box_font)


# Save the image as a high-quality JPEG with compression quality (1-95)
image.save("text_image.jpg", "JPEG", quality=100)
