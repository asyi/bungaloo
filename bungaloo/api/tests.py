from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.test import TestCase
from . models import Home

class ModelTestCase(TestCase):
    """This class defines the test suite for the home model."""

    def setUp(self):
        """Defines the test client and other test variables"""
        self.home = Home()