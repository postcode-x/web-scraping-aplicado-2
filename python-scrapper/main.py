import requests
from bs4 import BeautifulSoup
import json

json_data = []
max_pages = 4000
batch = max_pages
base = "https://www.antronio.cl/temas/"

for i in range(0, max_pages):

    result = requests.get(base + "exterminio-de-plagas-coronavirus-la-pandemia-del-covid-19.1317977/page-" + str(i + 1))

    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    timestamps = soup.find_all("time")
    page_timestamps = []

    for k in range(len(timestamps)):
        page_timestamps.append(timestamps[k]["data-time"])

    json_data.append({'page': i + 1, 'timestamps': page_timestamps})

    if len(json_data) == batch:
        with open('data/result3.json', 'w', encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=3)
        json_data = []
