from django.shortcuts import render

from .models import Article
from .parsing import articles
from django.core.paginator import Paginator


def index(request):
    all_articles = [Article(title=article['title'],
                            short_text=article['text'],
                            image=article['img'],
                            url=article['url'],
                            date=article['date'])
                    for article in articles]
    paginator = Paginator(all_articles, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'parsing/index.html', {'page': page,
                                                  'paginator': paginator,
                                                  'articles': all_articles})
