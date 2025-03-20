from django import forms
from first_app.models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        # fields = ['name', 'roll']
        # exclude = ['father_name']
        labels = {
            'name': 'Student Name',
            'roll': 'Roll Roll',
            'address': 'Address',
            'father_name': 'Father Name'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'btn-primary'}),
            # 'roll': forms.PasswordInput(),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control'})
        }
        help_texts = {
            'name': 'Enter your full name',
            'roll': 'Enter your roll number'
        }
        error_messages = {
            'name': {'required': 'Name is required'}
        }