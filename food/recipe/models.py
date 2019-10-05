from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True, unique=True)

    def __str__(self):
        return self.name


class Food(models.Model):
    title          = models.CharField(max_length=100)
    price          = models.FloatField()
    category       = models.ForeignKey(Category, on_delete=models.CASCADE)
    created        = models.DateTimeField(auto_now_add=True)
    updated        = models.DateTimeField(auto_now=True)
    active         = models.BooleanField(default=True)
    description    = models.TextField()
    image          = models.ImageField(blank=True, null=True)
    view           = models.PositiveIntegerField(default = 0,blank=True)



    class Meta():
        ordering = ('-created',)


    def __str__(self):
        return self.title
class Comment(models.Model):
    comments    = models.TextField()
    author     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank = True)
    post       = models.ForeignKey(Food, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post.title

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])


class Contact(models.Model):
    name = models.CharField(max_length=120, blank=True)
    email = models.EmailField(blank=True)
    subject = models.CharField(max_length=300)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name