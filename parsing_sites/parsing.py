import re

import requests
from slugify import slugify


host = 'https://www.ng.kz/'
response = requests.get(url=host)
regex = r"<div class=\"\w+\"><li class=\"\w+\"><span class=\"\w+\"><img width=70 height=70 src='(https://www\.ng\.kz/images/library/news_lenta/[\w\d/.]+)'></span><b><a class=art href='https://www\.ng\.kz/modules/news/article\.php\?storyid=\d+'>([\w\d\s.,%()+\":?!№«»-]+)</a></b><div class=news_time>([\w\d\s]+, \d\d:\d\d)</div><div style=\"text-align: justify;\"><a class=art href='(https://www\.ng\.kz/modules/news/article\.php\?storyid=\d+)'>([\w\d\s.,%()+\":?!№«»-]+)\.</a>"
matching_result = re.findall(regex, response.text)
articles = [{'img': image, 'title': title, 'date': date, 'url': url, 'text': text} for image, title, date,  url, text in matching_result]


for article in articles:
    image_url = article['img']
    image_response = requests.get(url=image_url)
    with open('photos/' + slugify(image_url)[:-10] + '.' +
              str(image_url.split('.')[-1]), 'wb') as img_file:
        img_file.write(image_response.content)

# article_regex = r"<p class=\"sign-content\">([\w\s.]+)</p>"
#
# for article in articles:
#     article_url = article['url']
#     article_response = requests.get(url=article_url)
#     result = re.search(article_regex, article_response.text)
#     print(result.group(1))
#     # articles.append({'author': result})



