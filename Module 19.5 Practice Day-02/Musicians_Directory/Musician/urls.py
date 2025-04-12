from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateMusicianView.as_view(), name='musicianpage'),
    path('edit/<int:id>/', views.EditMusicianView.as_view(), name='editmusician')
]
