from django.test import TestCase
from django.core.urlresolvers import reverse


class ShowBioTest(TestCase):

    def test_index_bio_template(self):
        response = self.client.get(reverse('index_bio'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hello/index.html', 'hello/base.html')

    def test_index_bio_hardcoded_data(self):
        response = self.client.get(reverse('index_bio'))
        self.assertContains(response, 'Name')
        self.assertContains(response, 'Email')
        self.assertContains(response, 'Surname')
        self.assertContains(response, 'JID')
        self.assertContains(response, 'Skype')
