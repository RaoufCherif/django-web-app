from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
 return HttpResponse('<h1>Hello L ILOT!<h1>')



def about(request):
    return HttpResponse('<h1>A propos</h1> <p>Nous adorons merch !</h2>')

