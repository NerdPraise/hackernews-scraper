from django.urls import path
from .views import NewsList, SearchNews

urlpatterns = [
    path('', NewsList.as_view(), name='news-list'),
    path('search/', SearchNews.as_view(), name='news-search'),
]
