# 4. Write a Python program to extract and display all the image links from
# en.wikipedia.org/wiki/Peter_Jeffrey_(RAAF_officer)


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html_data = urlopen(
    'https://en.wikipedia.org/wiki/Peter_Jeffrey_(RAAF_officer)')
bs = BeautifulSoup(html_data, 'html.parser')
allImages = bs.find_all('img', {'src': re.compile('.jpg')})
for pic in allImages:
    print(pic['src']+'\n')


# tried to load data in json but getting errors
# load = json.dumps({"image": allImages, "other_key": "value"})
# print(load)
