from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [

    path('', views.HomeListView.as_view(), name='home'),
    path('home', views.HomeListView.as_view(), name='home'),
    path('menu', views.MenuListView.as_view(), name='menu'),
    path('contact', views.ConatactCreateView.as_view(), name='contact'),
    path('about', views.about, name='about'),
    path('detail/<int:pk>', views.FoodDetailView.as_view(), name='detail'),
]
urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
