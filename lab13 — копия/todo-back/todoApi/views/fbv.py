from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from todoApi.models import TaskList
from todoApi.serializers import TaskListSerializer2


@api_view(['GET', 'POST'])
def task_list(request):
    if request.method == 'GET':
        categories = TaskList.objects.all()
        serializer = TaskListSerializer2(categories, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TaskListSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
def task_list_detail(request, pk):
    try:
        category = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return Response({'error': f'{e}'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskListSerializer2(category)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TaskListSerializer2(instance=category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)