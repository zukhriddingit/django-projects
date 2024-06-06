from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=300)
    published_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
        