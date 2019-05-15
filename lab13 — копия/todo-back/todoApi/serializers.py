from rest_framework import serializers
from todoApi.models import TaskList, Task
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)

class TaskListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    def create(self, validated_data):
        task = TaskList(**validated_data)
        task.save()
        return task

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class TaskListSerializer2(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    class Meta:
        model = TaskList
        fields = ('id', 'name')

class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    status = serializers.CharField(required=True)
    task_list = TaskListSerializer2()

    def create(self, validated_data):
        task = Task(**validated_data)
        task.save()
        return task

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance