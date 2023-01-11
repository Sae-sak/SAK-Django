from django.http import JsonResponse

from core.models import Project
from .serializers import ProjectSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def project_list(request, *args, **kwargs):

    if request.method == 'GET':
        projects = Project.objects.all().values()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=request.data, status=status.HTTP_201_CREATED)

