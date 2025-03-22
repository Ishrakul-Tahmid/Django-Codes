from django import forms
from .models import Author
# when we work on a class and want to extra characteristics we use Meta class
# Meta class is used to provide extra information about the class
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'