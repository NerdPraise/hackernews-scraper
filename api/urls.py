from django.urls import path, include

urlpatterns = [
    path('news/', include('api.news_scrape.urls'))
]
