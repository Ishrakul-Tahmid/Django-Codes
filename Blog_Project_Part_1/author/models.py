from django.db import models

# Create your models here.
# if char_field is used then max_length is required
class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()
    phone_no = models.CharField(max_length=12)

    def __str__(self):
        return self.name