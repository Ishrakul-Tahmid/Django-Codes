from django import forms
from .models import Profile
# when we work on a class and want to extra characteristics we use Meta class
# Meta class is used to provide extra information about the class
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'