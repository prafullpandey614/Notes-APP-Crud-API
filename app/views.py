from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,RetrieveAPIView,ListAPIView,UpdateAPIView
from .serializers import NoteSerializer
from .models import Note
from django.db.models import Q


class NotesAPIView(ListCreateAPIView):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    
class GetSingleNoteAPIView(RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_field = 'pk'
    
class NoteSearchAPIView(ListAPIView):
    serializer_class = NoteSerializer

    def get_queryset(self):
        queryset = Note.objects.all()
        title = self.request.query_params.get('title', None)  
        if title:
            queryset = queryset.filter(Q(title__icontains=title))  
        return queryset
    
class NotesUpdateAPIView(UpdateAPIView):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()  
    serializer_class = NoteSerializer 
    lookup_field = 'pk'  
    