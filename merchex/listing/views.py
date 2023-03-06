from django.shortcuts import render
from django.http import HttpResponse
from listing.models import Band
from listing.BandForm import BandForm 
from listing.forms import ContactUsForm
from django.core.mail import send_mail
from django.shortcuts import redirect

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

def contact(request):
    if request.method == 'POST':
         form = ContactUsForm(request.POST)
         if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
            message = form.cleaned_data['message'],
            from_email = form.cleaned_data['email'],
            recipient_list = ['admin@merchex.xyz'],
         )
         return redirect('confirm')
    else:
         form = ContactUsForm()

    return render(request,
            'listing/contact.html', {'form': form})

def confiramtion(request):
    return render(request,'listing/confirm_form.html')

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
        return redirect('confirm')
    else:
        form = BandForm()
        return render(request,
            'listing/band_create.html',
             {'form': form})