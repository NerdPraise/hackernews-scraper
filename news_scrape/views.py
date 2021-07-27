from django.shortcuts import render
from django.views.generic import ListView
from .models import News
# Create your views here.


class NewsList(ListView):
    template_name = 'home.html'
    queryset = News.objects.all()
    print(len(queryset))
    context_object_name = 'news'
    paginate_by = 15
