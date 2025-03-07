from rest_framework import viewsets
from .models import Student, Subject, Marks  # ✅ Ensure models are imported correctly
from .serializers import StudentSerializer, SubjectSerializer, MarksSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class MarksViewSet(viewsets.ModelViewSet):
    queryset = Marks.objects.all()
    serializer_class = MarksSerializer
