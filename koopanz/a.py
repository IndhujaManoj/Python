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

# Define the desired width and height (resolution)
desired_width = 1000
desired_height = 2000

# Screenshot the HTML content with the CSS and set the size
image = hti.screenshot(
    html_str=html_content,
    css_str=css_content,
    size=(desired_width, desired_height)
)

# Convert the image data to a PIL Image
pil_image = Image.frombytes("RGB", (desired_width, desired_height), image)

# Set the DPI for high quality (adjust as needed)
pil_image.info["dpi"] = (300, 300)  # Set to 300 DPI for example

# Save the high-quality image
pil_image.save("high_quality_screenshot.png")
