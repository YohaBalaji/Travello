from django.urls import path
from . import views

urlpatterns = [
    path('user',views.user, name='user'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('get',views.get, name = 'get'),
]