from django.test import TestCase
from . models import Home

class ModelTestCase(TestCase):
    """This class defines the test suite for the home model."""

    def setUp(self):
        """Defines the test client and other test variables"""
        self.home = Home()

    def test_model_can_create_a_home(self):
        """Tests the home model to see if it can create a home"""
        old_count = Home.objects.count()
        self.home.save()
        new_count = Home.objects.count()
        self.assertNotEqual(old_count, new_count)