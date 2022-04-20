from django.shortcuts import render

from .models import Article
from .parsing import articles


def index(request):
    all_articles = [Article(title=article['title'],
                            short_text=article['text'],
                            image=article['img'],
                            url=article['url'],
                            date=article['date'])
                    for article in articles]
    return render(request, 'parsing/index.html', {'articles': all_articles})
