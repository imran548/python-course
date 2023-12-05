
import warnings

warnings.filterwarnings('ignore', message='Unverified HTTPS request')
import base64
import requests
from amazon_paapi import AmazonApi

Base_url = "https://python.local/wp-json"
media_url =f'{Base_url}/wp/v2/media'
post_url =f'{Base_url}/wp/v2/post'
user = "imran"
password = "FjZF Fdkl kvAr j1VZ vC2V nszw"
credential = f'{user}:{password}'
token = base64.b64encode(credential.encode())
header = {'Authorization':f'Basic {token.decode("utf-8")}'}

def wp_post(post_url, data):
    res = requests.post(post_url,json=data, headers= header, verify=False )
    print( res.status_code)
def wp_h2(text):
    code = f' <!-- wp:heading --><h2 class="wp-block-heading">{text}</h2><!-- /wp:heading -->'
    return code
def wp_image(image_url):
    codes = f' <!-- wp:image {{"id":8,"sizeSlug":"full","linkDestination":"none"}} --><figure class="wp-block-image size-full"><img src="{image_url}" alt="" class="wp-image-8"/></figure><!-- /wp:image -->'
    return codes
def wp_list(py_list):
    list_html = "<!-- wp:list --> <ul>"
    for item in py_list:
        list_html += f' <!-- wp:list-item --><li>{item}</li><!-- /wp:list-item -->'
    list_html += "</ul><!-- /wp:list -->"
    return list_html


KEY = 'AKIAJIQ7AVH26LE5UTEA'
SECRET = "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"
TAG = 'automate0f-20'
COUNTRY = "US"

amazon = AmazonApi(KEY,SECRET,TAG,COUNTRY)
search_result = amazon.search_items(keywords="laptop")
#item = amazon.get_items("B09Q8PHT72")[0]
content = ''
for item in search_result.items:
    title = wp_h2(item.item_info.title.display_value)
    lagre_image = wp_image(item.images.primary.large.url)
    features = wp_list(item.item_info.features.display_values)
    content = title + lagre_image + features

data = {"title": "top 10 laptop",
        "content": content,
        "status":"publish",
       }
wp_post(post_url,data)




