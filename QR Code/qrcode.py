 
import pyqrcode
import random
import string
import subprocess
import json
import uuid

# Generate a random alphanumeric code of a specific length
code_length = 12  # You can adjust the length as needed
alphanumeric_code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(code_length))

# Data to send in the QR code
data = {
    "uuid": str(uuid.uuid4()),
    "name": "John Doe",
    "mob_num": "1234567890",
    "date":"16_10_2023",
    "bill_num": "B12345",
    "total_amount": 100.00
}

# Convert the data dictionary to a JSON string
json_data = json.dumps(data)

# Create the QR code
qr = pyqrcode.create(json_data)

# Generate the QR code image
qr.png('google.png', scale=10)
