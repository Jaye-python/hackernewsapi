from django.test import TestCase



# USE python manage.py test news

from news.models import News


class NewsModelTests(TestCase):

    def setUp(self):
        News.objects.create(hacker_id=300, api_created=False)
        
    
    def test_db_object_was_created_successfully(self):
        """
        we should be able to create db objects
        """
        
        news = News.objects.filter(hacker_id = '300')
        self.assertIs(news.exists(), True)
        
    
    def test_cannot_delete_objects_with_apicreated_set_to_false(self):
        """
        items with 'api_created' set to FALSE are not permitted to be deleted. Their delete URL should redirect to the home page and return
        status code of 302, a URL REDIRECTION code
        """

    
        url = 'http://127.0.0.1:8000/delete/300/'
        
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
