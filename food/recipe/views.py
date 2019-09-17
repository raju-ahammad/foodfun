from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Food, Category
# Create your views here.


class HomeListView(ListView):
    model     = Food
    template_name = 'home.html'
    context_object_name = 'food_list'


class FoodDetailView(DetailView):
    model    = Food
    template_name = 'detail.html'

    def get_object(self):
        object = super(FoodDetailView, self).get_object()
        object.view += 1
        object.save()
        return object


def contact(request):
    return render(request, 'contact.html', {})

def about(request):
    return render(request, 'contact.html', {})
