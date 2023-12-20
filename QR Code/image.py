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
qr.add_data('https://www.example.com')
qr.make(fit=True)
qr_image = qr.make_image(fill_color='black', back_color='white')


# Create a new image

width, height = 1200, 1000
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)

# Define fonts and sizes
title_font = ImageFont.truetype('./fonts/Montserrat,Roboto/Montserrat/static/Montserrat-Black.ttf', size=200)
description_font = ImageFont.truetype('DejaVuSans.ttf', size=12)
validation_font = ImageFont.truetype('DejaVuSans-Bold.ttf', size=10)

# Define colors
green_color = (0, 128, 0)
text_color = (0, 0, 0)
shadow_color = (200, 200, 200)

# Define text content
title_text = 'Your Title'
description_line1 = 'Your description goes here. You can write multiple lines if needed.'
validation = 'Coupon valid until 24 Oct, 2023'

# Position the box and text
box_x = 10
box_y = 10
box_width = width - 20
box_height = height - 20

title_x = box_x + 10
title_y = box_y + 10

# Draw a rounded rectangle using a custom function
def draw_rounded_rectangle(draw, xy, color, radius):
    x1, y1, x2, y2 = xy
    for i in range(radius):
        draw.arc((x1, y1, x1 + radius * 2, y1 + radius * 2), 180, 270, fill=color)
        draw.arc((x2 - radius * 2, y1, x2, y1 + radius * 2), 270, 0, fill=color)
        draw.arc((x1, y2 - radius * 2, x1 + radius * 2, y2), 90, 180, fill=color)
        draw.arc((x2 - radius * 2, y2 - radius * 2, x2, y2), 0, 90, fill=color)
        draw.rectangle([x1, y1 + radius, x2, y2 - radius], fill=color)
        draw.rectangle([x1 + radius, y1, x2 - radius, y2], fill=color)

# Draw the rounded green box
draw_rounded_rectangle(draw, [box_x, box_y, box_x + box_width, box_y + box_height], green_color, radius=10)

# Draw the title
draw.text((title_x, title_y), title_text, text_color, font=title_font)

# Position description text
desc1_x = box_x + 10
desc1_y = title_y + 40

# Wrap and add lines for description
description_lines_desc1 = textwrap.wrap(description_line1, width=30)

for i, line in enumerate(description_lines_desc1):
    line_x = box_x + 10
    line_y = desc1_y + i * description_font.getsize(line)[1]
    draw.text((line_x, line_y), line, text_color, font=description_font)

# Position validation text
validation_x = box_x + 10
validation_y = desc1_y + len(description_lines_desc1) * description_font.getsize(description_lines_desc1[0])[1] + 10

# Wrap validation text
validation_lines = textwrap.wrap(validation, width=40)

# Add wrapped lines for validation text
for i, line in enumerate(validation_lines):
    line_x = box_x + 10
    line_y = validation_y + i * validation_font.getsize(line)[1]
    draw.text((line_x, line_y), line, text_color, font=validation_font)

# Paste the QR code image
qr_image = qr_image.resize((100, 100))
image.paste(qr_image, (width - 120, height - 120))

# Create a shadow for the QR code and text
shadow = Image.new('RGB', image.size, shadow_color)
shadow.paste(image, (10, 10))
shadow = shadow.filter(ImageFilter.GaussianBlur(10))

# Paste the shadow behind the QR code and text
image = Image.blend(shadow, image, alpha=0.7)

# Save the image in high quality as a TIFF
image.save('coupon_with_design.png', quality=95)