import base64
import requests
from amazon_paapi import AmazonApi
KEY = 'AKIAJIQ7AVH26LE5UTEA'
SECRET = "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"
TAG = 'automate0f-20'
COUNTRY = "US"

amazon = AmazonApi(KEY,SECRET,TAG,COUNTRY)
search_result = amazon.search_items(keywords="laptop")
print(search_result)
                                    