from api.news_scrape.serializers import NewsSerializer
from news_scrape.models import News
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPaginator(PageNumberPagination):
    page_size = 100


class NewsListView(generics.ListCreateAPIView):
    pagination_class = CustomPaginator
    serializer_class = NewsSerializer
    queryset = News.objects.order_by('-date_created')
