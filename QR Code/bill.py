import requests
import json

url = 'https://ocr.asprise.com/api/v1/receipt'
image = 'tnbill.jpg'

# Send the POST request to the API
response = requests.post(url,
                         data={
                             'api_key': 'TEST',  
                             'recognizer': 'auto',
                             'ref_no': 'ocr_python_123'
                         },
                         files={
                             'file': open(image, 'rb')
                         })

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    
    # Check if 'receipts' is in the response
    if 'receipts' in data:
        receipts = data['receipts']

        # Check if there are any receipts
        if len(receipts) > 0:
            first_receipt = receipts[0]
            items = first_receipt.get('items', [])

            # Print receipt information
            print(f"Your purchase at {first_receipt['merchant_name']} ")
            for item in items:
                print(f"{item['description']} - {first_receipt['currency']} {item['amount']}")

            print("-" * 30)
            print(f"Total: {first_receipt['currency']} {first_receipt['total']}")
        else:
            print("No receipts found in the response.")
    else:
        print("No 'receipts' key found in the response.")
else:
    print(f"Request failed with status code {response.status_code}")

print("-" * 30)
