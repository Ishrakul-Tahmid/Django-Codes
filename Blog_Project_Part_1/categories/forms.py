from django import forms
from .models import Category
# when we work on a class and want to extra characteristics we use Meta class
# Meta class is used to provide extra information about the class
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'