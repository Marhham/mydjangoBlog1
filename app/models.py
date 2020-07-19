from django.db import models

class Article(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField()
    body = models.TextField()
    #date = models.DataTimeField(auto_now_add = True)
    # in add foto
    # add in aouther
    def __str__(self):
        return self.title
    def snippet(self):
        return self.body[0:50]+' ...'
