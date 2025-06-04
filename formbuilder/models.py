from django.db import models


class DynamicForm(models.Model):
    title = models.CharField(max_length=100)

class FormField(models.Model):
    FIELD_TYPES = [
        ('text', 'Text'),
        ('number', 'Number'),
        ('date', 'Date'),
        ('password', 'Password'),
    ]

    form = models.ForeignKey(DynamicForm, related_name='fields', on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=FIELD_TYPES)
    order = models.PositiveIntegerField()

class EmployeeRecord(models.Model):
    form = models.ForeignKey(DynamicForm, related_name='employees', on_delete=models.CASCADE)
    data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)