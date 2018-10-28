from django.db import models

# Create your models here.


STATUS_CHOICES = (
    ('Inprogress', 'inprogress'),
    ('COMPLETED', 'completed'),
    ('PENDING','pending')
)


class todo_model(models.Model):

    title = models.CharField(max_length=100, unique=True)
    task_description =models.TextField()
    task_status = models.CharField(max_length=100,choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task_name
