from django.contrib import admin

from parsing_sites.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_filter = ('date', 'title', 'sharing_count')


admin.site.register(Article, ArticleAdmin)
