import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from todoApi.models import TaskList
from todoApi.serializers import TaskListSerializer, TaskListSerializer2, TaskSerializer


@csrf_exempt
def task_list(request):
    if request.method == 'GET':
        categories = TaskList.objects.all()
        serializer = TaskListSerializer2(categories, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        body = json.loads(request.body)
        serializer = TaskListSerializer2(data=body)
        if serializer.is_valid():
            # create function from serializer
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    return JsonResponse({'error': 'bad request'})


@csrf_exempt
def task_list_detail(request, pk):
    try:
        category = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        serializer = TaskListSerializer(category)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        body = json.loads(request.body)
        serializer = TaskSerializer(instance=category, data=body)
        if serializer.is_valid():
            # update function from serializer
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        category.delete()
        return JsonResponse({})
    return JsonResponse({'error': 'bad request'})


def task(request, pk):
    try:
        category = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    products = category.products.all()
    serializer = TaskSerializer(products, many=True)
    return JsonResponse(serializer.data, safe=False)