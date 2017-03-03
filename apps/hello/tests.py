from django.test import TestCase
from django.urls import reverse


class ShowBioTest(TestCase):

    def test_index_bio_template(self):
        response = self.client.get(reverse('hello:index_bio'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'templates/index.html')
