from django.shortcuts import render
from django.views.generic import ListView
from .models import News
# Create your views here.


class NewsList(ListView):
    template_name = 'news_list.html'
    queryset = News.objects.all().order_by('-date_created')
    context_object_name = 'news'
    paginate_by = 20


class SearchNews(ListView):
    model = News
    template_name = 'news_list.html'

    def get_queryset(self):
        search_word = self.request.GET.get('search')
        queryset = News.objects.filter(
            title__icontains=search_word).order_by('date_created')
        return queryset
