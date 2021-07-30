from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path('news/', include('api.news_scrape.urls')),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('docs/',
         SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/',
         SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
