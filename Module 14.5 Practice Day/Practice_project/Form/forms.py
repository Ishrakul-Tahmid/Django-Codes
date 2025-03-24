from django import forms
from django.forms import NumberInput
import datetime

class Exampleform(forms.Form):
    name = forms.CharField(initial='Your Name')

    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))

    email = forms.EmailField(required=False,)

    aggree = forms.BooleanField()

    date = forms.DateField()
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))

    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))

    value = forms.DecimalField()
    
    message = forms.CharField(max_length=200, )
    messages = forms.CharField(min_length=10, )

    email1 = forms.EmailField(label = "Enter your email address")

    first_name = forms.CharField(initial = "Ishrakul Tahmid")

    aggree1 = forms.BooleanField(initial=True)

    day = forms.DateField(initial=datetime.date.today)

    FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
    ]
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)

    favorite_color1 = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)

    favorite_colors = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)

    favorite_colors2 = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES,)