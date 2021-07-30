from django.test import TestCase
from news_scrape.models import Comment, News

# Create your tests here.


class NewsView(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        news = News.objects.create(
            author='quickcheck', title='Hello world')
        news.save()
        news = News.objects.create(
            author='checkquick', title='Hello hi')
        news.save()

    def test_news_list(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_news_filter(self):
        print("Method: test_false_is_true.")
        self.assertTrue(False)

    def test_news_search(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)

    def test_date_convert_func(self):

