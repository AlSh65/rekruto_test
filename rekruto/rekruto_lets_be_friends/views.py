from django.http import HttpResponse
from django.shortcuts import render


def hello_rekruto(request):
    if request.method == 'GET':
        name = request.GET.get('name', 'Rekruto')
        message = request.GET.get('message', 'Давай дружить')
        return HttpResponse(f'Hello {name}! {message}!')
