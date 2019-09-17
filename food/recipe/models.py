from django.db import models


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
