from django.db import models

# Create your models here.
# keyword_search/modles.py
class Document(models.Model):
    word = models.CharField(max_length= 100)
    description = models.TextField()

    def __str__(self):
        return self.word