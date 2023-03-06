from django.shortcuts import render
from django.http import HttpResponse
from listing.models import Band


def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listing/band_list.html',
                    context={'bands': bands })

def band_detail(request, id):
     band = Band.objects.get(id=id)
     return render(request,
            'listing/band_detail.html',
                {'band': band})

def about(request):
    return HttpResponse('<h1>A propos</h1> <p>Nous adorons merch !</h1>')

