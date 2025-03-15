from django import forms
from django.core import validators

#widgets -> for changing the default widget/ field to html input
#label -> for changing the default label

class contactForm(forms.Form):
    name = forms.CharField(label='Full Name : ', initial='Ishrakul', help_text='Total length should be less than 70 char', required=False, widget=forms.Textarea(attrs={'id': 'text_area', 'class': 'class1 class2', 'placeholder': 'Enter your name: '})) #disabled=True
    # file = forms.FileField(label='User File')
    # email = forms.EmailField(label='User Email', max_length=100)
    # age = forms.IntegerField(label='User Age')
    # weight = forms.FloatField(label='User Weight')
    # balance = forms.DecimalField(label='User Balance')
    # email = forms.EmailField(label='User Email', max_length=100)
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'type': 'number'}))
    check = forms.BooleanField(label='User Check')
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    appointment = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'datetime-local'}))
    CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    select = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    MEAL = [('P', 'Pepperoni'), ('M', 'Mashroom'), ('B', 'Beef')]
    pizza = forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple)


# class StudentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)
#     # def clean_name(self):
#     #     valname = self.cleaned_data.get('name')
#     #     if len(valname) < 10:
#     #         raise forms.ValidationError('Name should be more than 10 char')
#     #     return valname
#     # def clean_email(self):
#     #     valemail = self.cleaned_data.get('email')
#     #     if '.com' not in valemail:
#     #         raise forms.ValidationError("Email should contain '.com'")
#     #     elif '@' not in valemail:
#     #         raise forms.ValidationError("Email should contain '@'")
#     #     return valemail
#     def clean(self):
#         cleaned_data = super().clean() #for getting all data
#         valname = self.cleaned_data['name']
#         valemail = self.cleaned_data['email']

#         if len(valname) < 10:
#             raise forms.ValidationError("Enter a name with at least 10 characters")

#         if '.com' not in valemail:
#             raise forms.ValidationError("Your email must contain .com")

def len_check(value):
    if len(value) < 10:
        raise forms.ValidationError("Enter a text with at least 10 characters")

class StudentData(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput, 
        validators=[validators.MinLengthValidator(10, message="Name should be more than 10 characters")]
    )

    text = forms.CharField(
        widget=forms.TextInput, 
        validators=[len_check]
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput, 
        error_messages={'invalid': "Enter a valid email address"}
    )
    
    age = forms.IntegerField(
        widget=forms.NumberInput, 
        validators=[validators.MinValueValidator(1, message="Age must be at least 1"),
                    validators.MaxValueValidator(100, message="Age must be below 100")]
    )

    file = forms.FileField(
        widget=forms.FileInput, 
        validators=[validators.FileExtensionValidator(['pdf', 'doc', 'docx'], message="Only pdf, doc, docx files are allowed")]
    )


class PasswordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        val_name = self.cleaned_data['name']
        val_pass = self.cleaned_data['password']
        val_conpass = self.cleaned_data['confirm_password']
        
        if val_conpass != val_pass:
            raise forms.ValidationError("Password doesn't match")
        if len(val_name) < 15:
            raise forms.ValidationError("Name must be at least 15 characters")