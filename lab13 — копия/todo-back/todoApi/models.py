from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TaskListCreator(models.Manager):
    def for_user(self, user):
        return self.filter(created_by=user)

class TaskCreator(models.Manager):
    def for_user(self, user):
        return self.filter(created_by=user)

class TaskList(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=2)

    objects = TaskListCreator()

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json_list(self):
        return {
            'id': self.id,
            'name': self.name,
            'create_by': self.created_by
        }


class Task(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    due_on = models.DateTimeField()
    status = models.CharField(max_length=40)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='tasks')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=2)

    objects = TaskCreator()

    def __str__(self):
        return '{} : {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status
        }

    def to_json_detail(self):
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at,
            'due_on': self.due_on,
            'status': self.status
        }

