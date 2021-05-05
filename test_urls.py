from django.test import TestCase
from django.urls import reverse

class UrlsTests(TestCase):
    def findand_status200(self):
        url = reverse('findand')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)