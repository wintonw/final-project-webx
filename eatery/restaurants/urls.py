from django.urls import include, path, reverse
from . import views

# app name
app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signUp/', views.signUp, name='signUp'),
    # path('weight/', , name='contactMe'),
]
