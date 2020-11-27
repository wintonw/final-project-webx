from django.urls import include, path, reverse
from . import views

# app name
app_name = 'restaurants'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginPage, name='login'),
    path('signUp/', views.signUp, name='signUp'),
    path('logout/', views.logoutUser, name='logout'),
    # customer post login
    path('orders/', views.orders, name='orders'),
    # path('weight/', , name='contactMe'),
]
