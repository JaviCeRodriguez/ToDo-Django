from django.db import models

class TaskState(models.Model):
    state = models.CharField(default='Backlog', max_length=200)

    def __str__(self):
        return self.state

class Task(models.Model):
    name = models.CharField(null=False, blank=False, max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    state = models.ForeignKey(TaskState, on_delete=models.CASCADE)

    def __str__(self):
        return self.name