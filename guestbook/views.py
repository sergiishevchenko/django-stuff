from django.shortcuts import render


def index(request):
    return render(request, 'guestbook/index.html')


def sign(request):
    return render(request, 'guestbook/sign.html')
