from PIL import Image, ImageDraw

# Create a new image with a white background
width, height = 800, 600
background_color = (255, 255, 255)
image = Image.new("RGB", (width, height), background_color)

# Create a drawing object to draw on the image
draw = ImageDraw.Draw(image)

# Draw a red rectangle on the image
rectangle_color = (255, 0, 0)
rectangle_coords = [(100, 100), (700, 500)]
draw.rectangle(rectangle_coords, fill=rectangle_color, outline=None)

# Save the image to a file
image.save("my_image.png")

# Show the image (optional)
image.show()
