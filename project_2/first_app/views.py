from django.shortcuts import render

def home(response):
    return render(response, "first_app/home.html")