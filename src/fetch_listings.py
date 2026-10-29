import os
import requests
import json
from datetime import datetime, timezone
from dotenv import load_dotenv

load_dotenv()

keystring = os.getenv("ETSY_API_KEY")
shared_secret = os.getenv("ETSY_SHARED_SECRET")

url = "https://api.etsy.com/v3/application/listings/active"
headers = {"x-api-key": f"{keystring}:{shared_secret}"}

response = requests.get(url, headers=headers, timeout=10, params={"keywords": "sunstone", "limit": "50"})
print(response.url)
print(response.json())

data = response.json()
print(data.keys())

print("count", data["count"])
print("Lenght of the listings:", len(data["results"]))

first = data["results"][0]
print("First fields of the first listing:", list(first.keys()))

print(json.dumps(first, indent=2, ensure_ascii=False))

price_amount = first["price"]["amount"] / first["price"]["divisor"] 
print(price_amount, first["price"]["currency_code"]) 

for listing in data["results"]:
    title = listing["title"][:50]
    tags = listing["tags"][1:5]
    materials = listing["materials"][1:5]
    price = listing["price"]["amount"]/listing["price"]["divisor"]
    currency = listing["price"]["currency_code"]
    ts = listing["original_creation_timestamp"]
    print(datetime.fromtimestamp(ts, tz=timezone.utc), title,"|", tags, "|", price, currency, materials)
    

keyword = "sunstone"

for listing in data["results"]:
    in_title = keyword in listing["title"].lower()
    in_tags = any(keyword in tag.lower() for tag in listing["tags"])
    in_materials = any(keyword in materials.lower() for materials in listing["materials"])
    in_description =  keyword in listing["description"].lower()

    print(listing["listing_id"], in_title, in_tags, in_materials, in_description)
    

'''
listing_id = 4543119014
url = f"https://api.etsy.com/v3/application/listings/{listing_id}"
response = requests.get(url, headers=headers, timeout=10)
print(response.status_code)
print(json.dumps(response.json(), indent=2, ensure_ascii=False))
'''
