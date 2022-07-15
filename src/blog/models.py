from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, related_name="blog_creator", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
