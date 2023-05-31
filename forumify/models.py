from django.db import models

from authorize.models import Person


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Topic(models.Model):
    title = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Person, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='topic_images', null=True, blank=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    content = models.TextField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    author = models.ForeignKey(Person, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50]

