from django.http import HttpResponse
from django.shortcuts import render


def users(request):
    return render(request, 'users/all_users.html')

def create_user(request):
    return HttpResponse('<h1>User was created<h1>')

def delete_uder(request):
    return HttpResponse('<h1>User was deleted<h1>')

