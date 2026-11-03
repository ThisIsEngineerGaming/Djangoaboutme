from django.test import TestCase
from django.urls import reverse


class PagesTests(TestCase):
    def test_all_pages_return_200(self):
        for name in ['about:home', 'about:me:biography', 'about:me:facts',
                     'about:city:info', 'about:city:places']:
            response = self.client.get(reverse(name))
            self.assertEqual(response.status_code, 200, name)
