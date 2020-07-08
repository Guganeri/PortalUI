from dotenv import load_dotenv
import requests
import json
import os
import pymongo

URL = os.getenv("URL")

load_dotenv()

url = os.getenv("URL")

print(url)

searchData = requests.get(f'{url}/v1/fontes')
print(searchData)

