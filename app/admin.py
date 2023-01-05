from django.contrib import admin
from .models import Property, PropertyType, Offer, Testimonial, Contact, JointVenture, BecomeBuyer



class PropertyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

# Register your models here.
admin.site.register(Property, PropertyAdmin)
admin.site.register((PropertyType, Offer, Testimonial, Contact, BecomeBuyer, JointVenture))