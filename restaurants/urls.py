from django.urls import include, path, reverse
from . import views

# app name
app_name = 'restaurants'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginPage, name='login'),
    path('signUp/', views.signUp, name='signUp'),
    path('logout/', views.logoutUser, name='logout'),
    path('menu/', views.menu, name='menu'),
    path('how-to/', views.howTo, name='howTo'),
    path('cart/', views.cart, name='cart'),
    # customer post login
    path('orders/', views.orders, name='orders'),
    path('orders/complete', views.complete, name='complete'),
    path('orders/<int:id>/', views.ordersDetails, name='ordersDetails'),
    # staff, manager
    path('dashboard/', views.dashboard, name='dashboard'),
    # test
    path('cartJSON/', views.cartJSON, name='cartJSON'),
    path('menu_items/<int:id>/', views.menu_items, name='menu_items'),
    path('test/', views.test, name='test'),
]
