# from html2image import Html2Image

# hti = Html2Image()

# # Define the paths to your HTML and CSS files
# html_file_path = 'page.html'
# css_file_path = 'page.css'

# # Read the HTML and CSS content from the files
# with open(html_file_path, 'r') as html_file:
#     html_content = html_file.read()

# with open(css_file_path, 'r') as css_file:
#     css_content = css_file.read()

# # Screenshot the HTML content with the CSS and save it as an image
# hti.screenshot(html_str=html_content, css_str=css_content, save_as='page.png')
from html2image import Html2Image
from PIL import Image

hti = Html2Image()

# Define the paths to your HTML and CSS files
html_file_path = 'page.html'
css_file_path = 'page.css'

# Read the HTML and CSS content from the files
with open(html_file_path, 'r') as html_file:
    html_content = html_file.read()

with open(css_file_path, 'r') as css_file:
    css_content = css_file.read()

# Screenshot the HTML content with the CSS and save it as an image
image = hti.screenshot(html_str=html_content, css_str=css_content, save_as='page.png')

# Open the image using Pillow
with Image.open('page.png') as img:
    # Specify the mobile size as 320x480 pixels
    mobile_size = (320, 480)

    # Resize the image to the mobile size with antialiasing
    img = img.resize(mobile_size)

    # Save the resized image
    img.save('mobile_page.png', 'PNG', quality=100)
