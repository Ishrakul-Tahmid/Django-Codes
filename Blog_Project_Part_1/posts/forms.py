from django import forms
from .models import Post
# when we work on a class and want to extra characteristics we use Meta class
# Meta class is used to provide extra information about the class
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'