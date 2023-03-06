from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from listing.models import Band, Listing


class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = '__all__'
    
  

   