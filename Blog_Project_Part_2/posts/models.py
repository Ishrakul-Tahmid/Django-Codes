from django.db import models
from categories.models import Category
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    # one posts can be in multiple categories and one category can have multiple posts
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # for one to many relationship or many to one relationship we use ForeignKey
    # on_delete=models.CASCADE means if author is deleted then all posts related to that author will be deleted
    # on_delete=models.SET_NULL means if author is deleted then all posts related to that author will be set to NULL

    def __str__(self):
        return self.title