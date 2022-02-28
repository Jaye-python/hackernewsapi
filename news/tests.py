from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from django.utils.crypto import get_random_string as g

# Create your tests here.
# python manage.py test polls

from news.models import News


class NewsModelTests(TestCase):

    def setUp(self):
        News.objects.create(hacker_id=300, api_created=True)
        # News.objects.create(name="cat", sound="meow")
    
    

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        # time = timezone.now() + datetime.timedelta(days=30)
        # future_question = News(api_created=False)
        # self.assertIs(future_question.was_published_recently(), False)
        # url = 'http://127.0.0.1:8000/delete/30465265/'
        # url = reverse('News:detail', args=(future_question.hacker_id,))
        # response = self.client.get(url)
        # self.assertEqual(response.status_code, 400)

        ns = News.objects.get(hacker_id = '300')
        self.assertIs(ns.api_created, False)
        # lion = News.objects.get(hacker_id=30999)
        
        # lion = News.objects.all()

        # self.assertEqual(lion.delete(), "This wasn't created via API or this news item does not exist. It may not be deleted. Thank you")
        # d = g(length=4)
        # print(d)
