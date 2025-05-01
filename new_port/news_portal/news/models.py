from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    POST_TYPES = [
        ('news', 'Новость'),
        ('article', 'Статья'),
    ]

    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post_type = models.CharField(max_length=10, choices=POST_TYPES)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title