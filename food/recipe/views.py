from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import Food, Category, Comment, Contact
from django.urls import reverse_lazy
from .forms import CommentForm
# Create your views here.


class HomeListView(ListView):
    model     = Food
    template_name = 'home.html'
    context_object_name = 'food_list'
    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        context['food'] = Food.objects.order_by('-created')[:9];
        return context



class MenuListView(ListView):
    model     = Food
    template_name = 'menu.html'
    context_object_name = 'food_list'
    def get_context_data(self, **kwargs):
        context = super(MenuListView, self).get_context_data(**kwargs)
        context['menu'] = Food.objects.order_by('-created')
        return context

class FoodDetailView(DetailView):
    model    = Food
    template_name = 'detail.html'

    def get_object(self):
        object = super(FoodDetailView, self).get_object()
        object.view = object.view + 1
        object.save()
        return object

    def post(self, request, *args, **kwargs):
        view = CommentView.as_view()
        return view(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(FoodDetailView, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.get_object())
        context['form'] = CommentForm
        context['recent'] = Food.objects.order_by('-created')[:4];
        context['popular'] = Food.objects.order_by('-view')[:4];

        return context


def about(request):
    return render(request, 'about.html', {})



""" Comment section View"""
class CommentView(CreateView):
    model = Comment
    fields = ['comments']
    template_name = 'detail.html'
    def form_valid(self, form):
        models_name = Comment()
        models_name.comments = self.request.POST['comments']
        models_name.author = self.request.user
        models_name.post = Food.objects.get(pk=self.kwargs['pk'])
        models_name.save()
        return redirect(self.get_success_url(id = self.kwargs['pk']))

    def get_success_url(self, **kwargs):
        if  kwargs != None:
            return reverse_lazy('detail', kwargs = {'pk': kwargs['id']})
        else:
            return reverse_lazy('detail', args = (self.object.id,))


class ConatactCreateView(CreateView):
    model = Contact
    fields = ('name', 'email', 'subject', 'message')
    success_url = reverse_lazy('home')
    template_name = ('contact.html')