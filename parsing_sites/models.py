from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=250,
                             verbose_name='title of an article')
    short_text = models.TextField(max_length=500,
                                  verbose_name='first lines of an article')
    image = models.ImageField(upload_to='photos/', verbose_name='main photo')
    date = models.DateTimeField()
    url = models.URLField(max_length=250, verbose_name='url of an article')
    sharing_count = models.IntegerField(verbose_name='number of sharing')

    class Meta:
        ordering = ('date', )

    def __str__(self):
        return self.title
