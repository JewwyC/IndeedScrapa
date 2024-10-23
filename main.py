import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup



def get_url (query, location):
    template = "https://www.indeed.com/jobs?q={}&l={}"
    return template.format(query, location)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
}

url = get_url('Amazon', 'Irvine')
response = requests.get(url, headers=headers)

print(response)