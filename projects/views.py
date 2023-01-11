from core.models import Project
from .serializers import ProjectSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics

class ProjectDetailAPIView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectCreateAPIView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)

