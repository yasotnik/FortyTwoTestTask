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


class BioModelTest(TestCase):

    def create_model_data(self, name='name', surname='surname', email='email@mail.com', jid='jid@42cc.co', skype='skype', dateofbirth='01.02.03'):
        return Bio.objects.create(name=name, surname=surname, email=email, jid=jid, skype=skype, dateofbirth=dateofbirth)

    def test_bio_creation(self):
        bio = self.create_model_data()
        self.assertTrue(isinstance(bio, Bio))
