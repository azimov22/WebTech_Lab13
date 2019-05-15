from django.http import Http404

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination

from todoApi.models import TaskList, Task
from todoApi.serializers import TaskListSerializer2, TaskSerializer


class TaskLists(generics.ListCreateAPIView):
    serializer_class = TaskListSerializer2
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return TaskList.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class TaskListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer2
    permission_classes = (IsAuthenticated,)


class TaskListOfTask(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Task.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
