from django.urls import path
from .views import *

urlpatterns = [
    path('',users, name='users'),
    path('create/',create_user, name = 'create_user'),
    path('delete',delete_uder,name = 'delete_user')
]