'''
### Welcome to images.py ###
Requests images from the Internet
'''

from PIL import Image
import requests
from io import BytesIO

url_flag = 'https://pbs.twimg.com/media/EFgibyUU8AA7zMc.jpg'
response = requests.get(url_flag)
smileyy = Image.open(BytesIO(response.content))
