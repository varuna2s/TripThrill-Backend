from django.contrib import admin
from .models import PropertyTypes
# Register your models here.

admin.site.register([PropertyTypes])


admin.site.site_header = "Tripthrill Property Booking Administration"