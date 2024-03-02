# from django.shortcuts import render
from inertia import render


def index(request):
    return render(request, 'Welcome')
