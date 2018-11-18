from rest_framework import generics
from . serializers import HomeSerializer
from . models import Home

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behaviour of our api"""
    queryset = Home.objects.all()[:0]
    serializer_class = HomeSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new home"""
        serializer.save()

class ListView(generics.ListAPIView):
    """This class lists all the homes"""
    queryset = Home.objects.all()
    serializer_class = HomeSerializer

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles GET, PUT and DELETE requests"""
    queryset = Home.objects.all()
    serializer_class = HomeSerializer