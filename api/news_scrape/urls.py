from django.urls import path
from .views import NewsDetailView, NewsListView

urlpatterns = [
    path('', NewsListView.as_view(), name='news-list'),
    path("detail/<int:pk>/", NewsDetailView.as_view(), name='news-detail')
]
