import os

from dotenv import load_dotenv
from wordpress import API

load_dotenv()

consumer_key = os.getenv('GF_CK')
consumer_secret = os.getenv('GF_CS')
url = os.getenv('GF_URL')

gfapi = API(
    url=url,
    api="wp-json",
    version='gf/v2',
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
)

entradas = gfapi.get('entries')

print(entradas.json()['total_count'])
print(entradas.json()['entries'])
