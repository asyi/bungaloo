from rest_framework import generics
from . serializers import HomeSerializer
from . models import Home

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behaviour of our api"""
    queryset = Home.objects.all()
    serializer_class = HomeSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new home"""
        serializer.save()