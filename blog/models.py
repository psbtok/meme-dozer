from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_pic = models.ImageField(null=True, blank=True,upload_to='post_pics')
    likes = models.ManyToManyField(User, related_name="blog_posts")

    def total_likes(self):
        return self.likes.count();

    def __str__(self):
        return self.title

    def get_api_like_url(self):
        return reverse('like-api-toggle', kwargs={'pk': self.pk})

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
