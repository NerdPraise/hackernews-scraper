from django.urls import path
from .views import NewsDetail, NewsList, SearchNews

urlpatterns = [
    path('', NewsList.as_view(), name='news-list'),
    path('search/', SearchNews.as_view(), name='news-search'),
    path('details/<int:pk>/', NewsDetail.as_view(), name='news-detail')
]
