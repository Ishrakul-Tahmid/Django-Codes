from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    d = {
        'value': ['a', 'b', 'c', 'd'],
        'num1': 4,
        'date': datetime.datetime.now,
        'val': '',
        'info': 
                [
                    {'name': 'zed', 'age': 19},
                    {'name': 'amy', 'age': 22},
                    {'name': 'joe', 'age': 31},
                ],
        'joinval': ['a', 'b', 'c'],
        'jval': [['a', 'b', 'c'],
                 ['a', 'b', 'c'],
                 ['a', 'b', 'c']],
        'var': ['States', ['Kansas', ['Lawrence', 'Topeka'], 'Illinois']],

    }
    return render(request, 'home.html', context=d)