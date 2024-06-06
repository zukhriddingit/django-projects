from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=200)
    users = models.ManyToManyField(User, related_name='custom_groups')
    
    def __str__(self):
        return self.name

class Message(models.Model):
    author = models.ForeignKey(User, related_name='author_message', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE, null=True, blank=True) 
    group = models.ForeignKey(Group, related_name='messages', on_delete=models.CASCADE)
    text = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text

