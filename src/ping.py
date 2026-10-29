import os
import requests
from dotenv import load_dotenv

load_dotenv()

keystring = os.getenv("ETSY_API_KEY")
shared_secret = os.getenv("ETSY_SHARED_SECRET")

url = "https://api.etsy.com/v3/application/openapi-ping"
headers = {"x-api-key": f"{keystring}:{shared_secret}"}

response = requests.get(url, headers=headers, timeout=10)

print(response.status_code)
print(response.json())
