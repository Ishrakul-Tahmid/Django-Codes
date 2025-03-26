from django.db import models
from Task .models import TaskModel
# Create your models here.


class CategoryModel(models.Model):
    category_name = models.CharField(max_length=100)
    tasks = models.ManyToManyField(TaskModel)

    def __str__(self):
        return self.category_name