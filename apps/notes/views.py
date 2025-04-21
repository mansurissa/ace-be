from rest_framework import viewsets
from apps.notes.models import Note
from apps.notes.serializers import NoteSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all().order_by('-created_at')
    serializer_class = NoteSerializer
