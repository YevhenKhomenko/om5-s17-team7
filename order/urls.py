from . import views
from django.urls import path
urlpatterns = [
    path('', views.first_view,name='orders'),
    path('bad_users/', views.bad_users),

]