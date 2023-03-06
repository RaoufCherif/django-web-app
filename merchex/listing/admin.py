from django.contrib import admin
from listing.models import Band
from listing.models import Listing

class BandAdmin(admin.ModelAdmin):
 list_display = ('name', 'year_formed', 'genre')

admin.site.register(Band, BandAdmin)

class ListingAdmin(admin.ModelAdmin):
 list_display = ('title','version')
        
admin.site.register(Listing, ListingAdmin)


