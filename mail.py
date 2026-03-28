import os
import requests
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get URL from environment
url = os.getenv("URL")  # make sure key is URL in .env

# Payload (data sent to Apps Script)
payload = {
    "to": "", 
    "subject": "hello boyssss🚀",
    "body": "This email was sent dynamically from Python!"
}

# Send POST request
response = requests.post(url, json=payload)

# Output
print("Status:", response.status_code)
print("Response:", response.text)