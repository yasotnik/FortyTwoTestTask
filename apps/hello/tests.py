from django.test import TestCase
from django.core.urlresolvers import reverse
from .models import Bio


class ShowBioTest(TestCase):
    """Testing the show bio template

    Testing the hardcoded data for template

    """

    def setUp(self):
        """
        Creating a data in DB for template
        """
        self.bio = Bio.objects.create(name='name', surname='surname',
                                      email='email@mail.com',
                                      jid='jid@42cc.co',
                                      skype='skype', dateofbirth='2000-02-03')

    def test_index_bio_template(self):
        """Testing usage of the needed templates.

        First checking the status code, then checking templates.

        """
        response = self.client.get(reverse('index_bio'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hello/index.html',
                                'hello/base.html')

    def test_index_bio_hardcoded_data(self):
        """Testing hardcoded data in template.

        Testing that hardcoded data is in response

        """
        response = self.client.get(reverse('index_bio'))
        self.assertContains(response, 'Name')
        self.assertContains(response, 'Email')
        self.assertContains(response, 'Surname')
        self.assertContains(response, 'JID')
        self.assertContains(response, 'Skype')


class BioModelTest(TestCase):
    """Test for the Bio model.

    """

    def create_model_data(self, name='name', surname='surname',
                          email='email@mail.com', jid='jid@42cc.co',
                          skype='skype', dateofbirth='2000-02-03'):
        """Creating initial data for testing.

        :param name: Name of the person
        :param surname: Surname of the person
        :param email: Email of the person
        :param jid: JID of the person
        :param skype: Skype of the person
        :param dateofbirth: Date of birth of the person
        :return: Bio object
        """
        return Bio.objects.create(name=name, surname=surname,
                                  email=email, jid=jid, skype=skype,
                                  dateofbirth=dateofbirth)

    def test_bio_creation(self):
        """Testing that we will receive a Bio model.

        Creating the model then checking it

        """
        bio = self.create_model_data()
        self.assertTrue(isinstance(bio, Bio))


class BioModelDataInTemplateTest(TestCase):

    def setUp(self):
        """
        Creating a data in DB for template
        """
        self.bio = Bio.objects.create(name='name', surname='surname',
                                      email='email@mail.com',
                                      jid='jid@42cc.co',
                                      skype='skype', dateofbirth='2000-02-03')

    def test_model_data_in_template(self):
        """Testing if data from db is in template.

        Comparison of object with
        the response of rendering the template.

        """
        response = self.client.get(reverse('index_bio'))
        self.assertContains(response, 'Name: ' + self.bio.name)
        self.assertContains(response, 'Surname: ' + self.bio.surname)
