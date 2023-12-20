import qrcode

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,  # QR code version (adjust as needed)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box or module in pixels
    border=4,  # Border size around the QR code
)

# Add data to the QR code (e.g., a URL or text)
data = "https://www.google.com"
qr.add_data(data)

# Generate the QR codehow to generate the coopen image in python
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file
img.save("qrcode.png")

# Show the image (optional)
img.show()
