import qrcode
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import textwrap

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

# Create a new image
image = Image.new('RGB', (200, 400), (255, 255, 255))

# Create a draw object
draw = ImageDraw.Draw(image)

# Define fonts and sizes
title_font = ImageFont.truetype('DejaVuSans-Bold.ttf', size=20)
description_font = ImageFont.truetype('DejaVuSans.ttf', size=12)
validation_font = ImageFont.truetype('DejaVuSans-Bold.ttf', size=8)  # Adjust size as needed for bold text

# Define the background color
green_color = (0, 128, 0)  # RGB color for green

# Add text
title_text = 'Sundar Retails'
description_line1 = 'Your trusted health partner for pharmaceutical needs and expert care'
validation = 'Coupon valid up to 24 Oct, 2023'

# Calculate desc1_height
desc1_width, desc1_height = draw.textsize(description_line1, font=description_font)

# Define maximum line width for description 1 and wrap the text
max_line_width_desc1 = 250
description_lines_desc1 = textwrap.wrap(description_line1, width=30)  # Adjust the width as needed

# Calculate the total height needed for the wrapped text in description 1
total_text_height_desc1 = len(description_lines_desc1) * desc1_height

# Position the box and text
box_x = 10
box_y = 10  # Adjust to place the box at the top
box_width = 180
box_height = total_text_height_desc1 + 50  # Adjust as needed
border_radius = 10  # Adjust the border radius as needed

title_x = box_x + 10
title_y = box_y + 10

# Draw a rounded green box that covers title and description 1
draw.rounded_rectangle(
    [box_x, box_y, box_x + box_width, box_y + box_height],
    fill=green_color,
    outline=None,
    radius=border_radius,
)

# Draw the title
draw.text((title_x, title_y), title_text, (0, 0, 0), font=title_font)

# Position description 1 text
desc1_x = box_x + 10
desc1_y = title_y + 40  # Adjust as needed

# Add wrapped lines for description 1
for i, line in enumerate(description_lines_desc1):
    line_x = box_x + 1
    line_y = desc1_y + i * desc1_height
    draw.text((line_x, line_y), line, (0, 0, 0), font=description_font)

# Position validation text
validation_x = box_x + 10
validation_y = desc1_y + total_text_height_desc1 + 10

# Wrap validation text
max_line_width_validation = 180
validation_lines = textwrap.wrap(validation, width=40)  # Adjust the width as needed

# Add wrapped lines for validation text
for i, line in enumerate(validation_lines):
    line_x = box_x + 10
    line_y = validation_y + i * validation_font.getsize(line)[1]
    draw.text((line_x, line_y), line, (0, 0, 0), font=validation_font)

# Paste the QR code image
qr_image = qr_image.resize((100, 100))
image.paste(qr_image, (50, box_y + box_height + 30))  # Adjust the position as needed

# Create a shadow for the QR code and text
shadow = Image.new('RGB', image.size, (200, 200, 200))
shadow.paste(image, (10, 10))
shadow = shadow.filter(ImageFilter.GaussianBlur(10))

# Paste the shadow behind the QR code and text
image = Image.blend(shadow, image, alpha=0.7)

# Save the image
image.save('coupon_with_design.png')
