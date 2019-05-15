from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from todoApi.models import TaskList
from todoApi.serializers import TaskListSerializer2
from django.views.decorators.csrf import csrf_exempt


class TaskLists(APIView):
    def get(self, request):
        taskList = TaskList.objects.all()
        serializer = TaskListSerializer2(taskList, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskListSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TaskListDetail(APIView):

    def get_object(self, pk):
        try:
            return TaskList.objects.get(id=pk)
        except TaskList.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        taskList = self.get_object(pk)
        serializer = TaskListSerializer2(taskList)
        return Response(serializer.data)

    def put(self, request, pk):
        taskList = self.get_object(pk)
        serializer = TaskListSerializer2(instance=taskList, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        taskList = self.get_object(pk)
        taskList.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)