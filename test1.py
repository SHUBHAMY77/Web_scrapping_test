import re


def date(url):
    return re.findall(r'/(\d{4})/(\d{2})/(\d{2})/', url)


url1 = "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"
print('year, month and date from string are :-', date(url1))
