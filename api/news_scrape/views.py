from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from api.news_scrape.serializers import NewsSerializer
from news_scrape.models import News
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPaginator(PageNumberPagination):
    page_size = 50


class NewsListView(generics.ListCreateAPIView):
    """
    View all news present in the database or create new list
    """
    pagination_class = CustomPaginator
    serializer_class = NewsSerializer
    queryset = News.objects.order_by('-date_created')

    filter_fields = (
        'author',
        'type',
        'is_posted',
    )

    def perform_create(self, serializer):
        is_posted = serializer.validated_data.get('is_posted')
        is_posted = True
        serializer.save(is_posted=is_posted)


class NewsDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update or Delete a particular news
    """
    serializer_class = NewsSerializer
    queryset = News.objects.get_queryset()

    def update(self, request, *args, **kwargs):
        news_id = kwargs.get('pk')
        try:
            news = News.objects.get(id=news_id)
            if not news.is_posted:
                return Response(
                    {'message': 'You can not edit an item that is not manually posted'},
                    status=HTTP_400_BAD_REQUEST)

            return super(NewsDetailView, self).update(request, *args, **kwargs)
        except News.DoesNotExist:
            return Response({'message': 'Item does not exist'}, status=HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        news_id = kwargs.get('pk')
        try:
            news = News.objects.get(id=news_id)
            if not news.is_posted:
                return Response({'message': 'You can not delete an item that is not manually posted'}, status=HTTP_400_BAD_REQUEST)
    
            return super(NewsDetailView, self).delete(request, *args, **kwargs)
        except News.DoesNotExist:
            return Response({'message': 'Item does not exist'}, status=HTTP_404_NOT_FOUND)
