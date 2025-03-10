
from django.urls import path
# from first_app.views import views
# from first_app import views
from . import views # here .(dot) means from this app

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home),
]
