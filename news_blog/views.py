from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound 
from .models import Article, Author, Comment

def index(request):
    articles = Article.objects.order_by("created_date")
    return render(request, 'news_blog/news_list.html', 
                {
                    "articles": articles,
                    "count_articles": len(articles)
                })

def get_article(request, article_id):
    try:
        article = Article.objects.get(id = article_id)
        bauthor = Author.objects.filter(article__pk = article_id)
        comments = Comment.objects.filter(article = article_id)
    except Article.DoesNotExist:
        return HttpResponseNotFound()
    return render(request, 'news_blog/news_article.html', {'article': article,'author': bauthor,'comments': comments})

def get_about(request):
    return render(request, 'news_blog/about.html')
