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

@api_view(['GET', 'PUT', 'DELETE'])
def project_detail(request, id):

    try:
        project = Project.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serialize = ProjectSerializer(project)
        return Response(serialize.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serialize = ProjectSerializer(project, data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
    elif request.method == "DElETE":
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)