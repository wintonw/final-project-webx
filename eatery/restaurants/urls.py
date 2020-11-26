from django.urls import include, path, reverse
from . import views

# app name
app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    # path('weight/', , name='contactMe'),
]
