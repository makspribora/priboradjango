from django.contrib import admin
from .models import Article, Author, Comment

# Register your models here.
admin.site.register([Article, Author, Comment])

