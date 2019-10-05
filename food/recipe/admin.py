from django.contrib import admin

from .models import Food, Category, Comment, Contact

admin.site.register(Food)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Contact)


