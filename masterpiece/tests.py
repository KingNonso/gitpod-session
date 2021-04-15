from django.core.exceptions import ValidationError
from django.test import TestCase, Client

from masterpiece.models import Contact
from . import views


class ContactTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        Contact.objects.create(subject="lion", body="roar")
        Contact.objects.create(subject="cat", body="meow")

    def test_contact_with_subject_passes(self):
        """Contacts that can speak are correctly identified"""
        lion = Contact.objects.get(subject="lion")
        cat = Contact.objects.get(subject="cat")
        self.assertEqual(lion.speak, 'roar')
        self.assertEqual(cat.speak, 'meow')


class StandardPythonTest(TestCase):
    def test_two_plus_two_passes(self):
        self.assertEqual(views.standard_python(), 4)

    def test_two_plus_two_fails(self):
        self.assertNotEqual(views.standard_python(), 5)

