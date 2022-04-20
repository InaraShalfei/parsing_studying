import re
from hashlib import md5

import requests
from slugify import slugify

from pandas.io.common import file_exists


def get_content_by_url(url, as_binary):
    filename = '/tmp/' + md5(url.encode('utf-8')).hexdigest()
    if not file_exists(filename):
        response = requests.get(url=url)
        if as_binary:
            with open(filename, 'wb') as file:
                file.write(response.content)
        else:
            with open(filename, 'w') as file:
                file.write(response.text)

    if as_binary:
        content_file = open(filename, 'rb')
        content = content_file.read()
    else:
        content_file = open(filename, 'r')
        content = str(content_file.read())

    content_file.close()
    return content


host = 'https://www.ng.kz/'
response = get_content_by_url(host, False)
regex = r"<div class=\"\w+\"><li class=\"\w+\"><span class=\"\w+\"><img width=70 height=70 src='(https://www\.ng\.kz/images/library/news_lenta/[\w\d/.]+)'></span><b><a class=art href='https://www\.ng\.kz/modules/news/article\.php\?storyid=\d+'>([\w\d\s.,%()+\":?!№«»-]+)</a></b><div class=news_time>([\w\d\s]+, \d\d:\d\d)</div><div style=\"text-align: justify;\"><a class=art href='(https://www\.ng\.kz/modules/news/article\.php\?storyid=\d+)'>([\w\d\s.,%()+\":?!№«»-]+)\.</a>"
matching_result = re.findall(regex, response)
articles = [{'img': image, 'title': title, 'date': date, 'url': url, 'text': text} for image, title, date,  url, text in matching_result]


for article in articles:
    image_url = article['img']
    image_response = get_content_by_url(image_url, True)
    with open('photos/' + slugify(image_url)[:-10] + '.' +
              str(image_url.split('.')[-1]), 'wb') as img_file:
        img_file.write(image_response)

# article_regex = r"<p class=\"sign-content\">([\w\s.]+)</p>"
#
# for article in articles:
#     article_url = article['url']
#     article_response = requests.get(url=article_url)
#     result = re.search(article_regex, article_response.text)
#     print(result.group(1))
#     # articles.append({'author': result})



