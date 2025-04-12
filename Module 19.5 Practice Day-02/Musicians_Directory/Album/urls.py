from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateAlbum.as_view(), name='albumpage'),
    path('edit/<int:id>', views.EditAlbumView.as_view(), name='editalbum'),
    path('delete/<int:id>', views.DeleteAlbumView.as_view(), name='deletealbum'),
]