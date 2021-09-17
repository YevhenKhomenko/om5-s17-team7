from . import views
from django.urls import path
urlpatterns = [
    path('', views.first_view),
    path('author/', views.by_author),
    path('user/', views.by_user),
    path('detail/', views.detail),
    path('detail/<received_id>', views.detail),
path('unordered/', views.unordered),


]