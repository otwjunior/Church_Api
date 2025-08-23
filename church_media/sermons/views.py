from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Sermon
from .serializers import SermonSerializer

# List all sermons / create a new sermon
class SermonListCreateView(generics.ListCreateAPIView):
    queryset = Sermon.objects.all()
    serializer_class = SermonSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)

# Retrieve, update, delete a specific sermon
class SermonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sermon.objects.all()
    serializer_class = SermonSerializer
    permission_classes = [permissions.IsAuthenticated] #only login user  can delete/update

    # restrict update/delete to the user who added it
    def get_queryset(self):
        user = self.request.user
        return Sermon.objects.filter(added_by=user)
