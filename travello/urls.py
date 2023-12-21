from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('',views.index, name='index'),
    path('post/',views.post_val, name='post'),
    path('view/',views.view, name='view'),
    path('delete/',views.delid, name='delid'),
    path('update/',views.updateByID, name='updateByID'),
]
