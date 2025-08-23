from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Song
from .serializers import SongSerializer

# List all songs / create a new song
class SongListCreateView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [permissions.IsAuthenticatedOrRedOnly]  # only logged-in users can add/create new song

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)  # set added_by automatically

    # serch by title or category
    def get_queryset(self):
        queryset= Song.objects.all()
        title = self.request.query_params.get("title")
        category = self.request.query_params.get("category")

        if title:
            queryset = queryset.filter(title_icontins=title)
        if category:
            queryset = queryse.filter(category_icontains=category)
        return queryset
# Retrieve, update, delete a specific song
class SongDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [permissions.IsAuthenticated]

    # restrict update/delete to the user who added it
    def get_queryset(self):
        user = self.request.user
        return Song.objects.filter(added_by=user)  # only user's songs

