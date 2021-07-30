from django.forms.fields import DateTimeField
from news_scrape.utils import unix_to_datetime
from django.test import TestCase
from django.urls import reverse
from news_scrape.models import Comment, News

# Create your tests here.


class NewsView(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        number_of_news = 25  # To test pagination

        for news_id in range(number_of_news):
            News.objects.create(
                author=f'quickcheck{news_id}',
                title=f'Hello Dear {news_id}',
                type='story')

    def test_news_list_pagination(self):
        response = self.client.get(reverse('news-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['news_list']), 20)

    def test_correct_template_view(self):
        response = self.client.get(reverse('news-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news_list.html')

        response = self.client.get(reverse('news-detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news_detail.html')

    def test_news_filter(self):
        response = self.client.get(reverse('news-list')+'?type=story')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['news_list']), 20)

    def test_news_search(self):
        response = self.client.get(reverse('news-list')+'?search=2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['news_list']), 1)

    def test_date_convert_func(self):
        unix_time = 3483204
        # call the function
        response = unix_to_datetime(unix_time)
        self.assertEqual(type(response), DateTimeField)
