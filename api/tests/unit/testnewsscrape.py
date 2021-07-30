from news_scrape.models import News
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class NewsTestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.list_url = reverse('news-list-api')
        number_of_news = 5

        for news_id in range(number_of_news):
            news = News.objects.create(
                author=f'quickcheck{news_id}',
                title=f'Hello Dear {news_id}',
                type='story')
            news.save()

    news_create_data = {
        "type": "story",
        "author": "quickcheck",
        "date_created": "2021-07-30T06:20:46.821Z",
        "score": 3,
        "url": "www.purereact.com",
        "title": "Pure rage of react native"
    }

    update_data = {
        "title": "Updated pure rage"
    }

    def test_news_api_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 5)

    def test_news_create(self):
        response = self.client.post(self.list_url, self.news_create_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['type'], 'story')

        # assert that is_posted is true by default
        self.assertTrue(response.data['is_posted'])

    def test_news_update(self):
        # call test news create for the data
        response = self.client.post(self.list_url, self.news_create_data)
        news_id = response.data['id']
        response = self.client.patch(
            reverse('news-detail-api', args=(news_id,)), self.update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_news_delete(self):
        news = self.client.post(
            reverse('news-list-api'), self.news_create_data)
        news_id = news.data['id']
        response = self.client.delete(
            reverse('news-detail-api', args=(news_id,)))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_filter_news(self):
        response = self.client.get(reverse('news-list-api')+'?type=story')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_edit_scraped_news(self):
        response = self.client.patch(
            reverse('news-detail-api', args=(1,)), self.update_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data['message'], 'You can not edit an item that is not manually posted')
