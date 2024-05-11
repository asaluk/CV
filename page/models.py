from django.db import models

# Create your models here.

class Comment(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    opinion = models.TextField()
    def __str__(self):
        return self.name
    