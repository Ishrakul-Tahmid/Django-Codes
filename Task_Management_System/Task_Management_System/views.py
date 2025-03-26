from django.shortcuts import render
from Category.models import CategoryModel


def home(request):
    alltasks = CategoryModel.objects.all()
    return render(request, 'home.html', {'alltasks': alltasks})