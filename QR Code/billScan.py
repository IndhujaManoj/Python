import json
import requests

# url='https://ocr.asprise.com/api/v1/receipt'
# image='wallmart.jpg'

# res=requests.post(url,
#                   data={
#                       'api_ket':'TEST',
#                       'recognizer':'auto',
#                       'ref_no':'ocr_python_123'
#                   },
#                   files={
#                       'file':open(image,'rb')
#                   })

# with open("response2.json","w") as f:
#     json.dump(json.loads(res.text),f)


with open('response1.json') as f:
    data = json.load(f)
    print(data['receipts'][0].keys())
    items=data['receipts'][0]['items']
    print(items)
    print(f"your purchase at {data['receipts'][0]['merchant_name']} ")
for item in items:
    print(f"{item['description']} - {data['receipts'][0]['currency']} {item['amount']}")

print("-"*30)
print(f"Total:- {data['receipts'][0]['currency']} {data['receipts'][0]['total']}")
 


print("-"*30)
 