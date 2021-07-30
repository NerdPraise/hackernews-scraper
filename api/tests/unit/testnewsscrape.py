from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class NewsTestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = APIClient()
        cls.list_url = reverse('news-list')

    news_create_data = {
        "type": "story",
        "author": "quickcheck",
        "date_created": "2021-07-30T06:20:46.821Z",
        "score": 3,
        "url": "www.purereact.com",
        "title": "Pure rage of react native"
    }

    def test_news_api_list(self):
        pass

    def test_news_create(self):
        pass

    def test_news_update(self):
        pass

    def test_news_delete(self):
        pass

    def test_filter_news(self):
        pass
