from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Comment, News
# Create your views here.


class NewsList(ListView):
    template_name = 'news_list.html'
    queryset = News.objects.all().order_by('-date_created')
    context_object_name = 'news'
    paginate_by = 20

    def get_queryset(self):
        filter_param = self.request.GET.get('news_type')
        if filter_param:
            queryset = News.objects.filter(
                type=filter_param).order_by('date_created')
        else:
            queryset = News.objects.all().order_by('-date_created')
        return queryset


class SearchNews(ListView):
    model = News
    template_name = 'news_list.html'
    context_object_name = 'news'
    paginate_by = 20

    def get_queryset(self):
        search_word = self.request.GET.get('search')
        queryset = News.objects.filter(
            title__icontains=search_word).order_by('date_created')
        return queryset


class NewsDetail(DetailView):
    model = News
    template_name = 'news_detail.html'
    context_object_name = 'details'

    def get_context_data(self, **kwargs):
        news_id = kwargs.get('object').id
        news = News.objects.get(pk=news_id)
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(parent=news.item_id)
        return context
