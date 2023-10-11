
import pyqrcode
import random
import string
import subprocess
# Generate a random alphanumeric code of a specific length
code_length = 12 # You can adjust the length as needed
alphanumeric_code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(code_length))


# Create the QR code
qr = pyqrcode.create(alphanumeric_code)

# Generate the QR code image
qr.png('google.png', scale=10)

      
