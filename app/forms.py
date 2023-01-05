from django import forms
from .models import Contact, Offer, BecomeBuyer, JointVenture
from django.conf import settings

class ContactForm(forms.ModelForm):
    name = forms.CharField(required=True,)
    email = forms.EmailField(required=True,)
    subject = forms.CharField(required=True,)
    message = forms.CharField(required=True,)
    class Meta():
        model = Contact
        fields = ('name', 'email', 'subject', 'message')

class OfferForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    name = forms.CharField(required=True)
    message = forms.CharField(required=True,)
    class Meta():
        model = Offer
        fields = ('email', 'name', 'message',)

class BecomeBuyerForm(forms.ModelForm):
    # first_name = forms.CharField(required=True)
    # last_name = forms.CharField(required=True)
    # email = forms.EmailField(required=True)
    # phone = forms.CharField(required=True)
    # company_name = forms.CharField(required=True)
    # area_buying = forms.CharField(required=True)
    # property_address = forms.CharField(required=False)
    # note = forms.CharField(required=False)
    class Meta():
        model = BecomeBuyer
        fields = (
            'first_name', 
            'last_name', 
            'email', 
            'phone', 
            'company_name', 
            'area_buying', 
            'property_address', 
            'note')
    
class JointVentureForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)
    company_name = forms.CharField(required=True)
    property_address = forms.CharField(required=True)
    sq_footage = forms.CharField(required=True)
    acquisition_price = forms.IntegerField(required=True)
    asking_price = forms.IntegerField(required=True)
    arv = forms.IntegerField(required=False)
    year_build = forms.IntegerField(required=True)
    year_roof = forms.IntegerField(required=True)
    year_hvac = forms.IntegerField(required=True)
    bedrooms = forms.IntegerField(required=True)
    bathrooms = forms.IntegerField(required=True)
    comp1_link = forms.URLField(required=True)
    comp1_price = forms.IntegerField(required=True)
    comp2_link = forms.URLField(required=False)
    comp2_price = forms.IntegerField(required=False)
    comp3_link = forms.URLField(required=False)
    comp3_price = forms.IntegerField(required=False)
    photo_link = forms.URLField(required=True)
    inspection_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=True)
    closing_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=True)
    occupancy = forms.CharField(required=True)
    hoa = forms.CharField(required=False)
    how_much = forms.CharField(required=False)
    payment_plan = forms.CharField(required=False)
    access = forms.CharField(required=True)
    date_aggreement = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=True)
    agreement_document = forms.FileField(required=True)
    property_note = forms.CharField(required=False)
    class Meta():
        model = JointVenture
        fields = (
            'first_name', 
            'last_name', 
            'email', 
            'phone', 
            'company_name',  
            'property_address',
            'sq_footage',
            'acquisition_price',
            'asking_price',
            'arv',
            'year_build',
            'year_roof',
            'year_hvac',
            'bedrooms',
            'bathrooms',
            'comp1_link',
            'comp1_price',
            'comp2_link',
            'comp2_price',
            'comp3_link',
            'comp3_price',
            'photo_link',
            'inspection_date',
            'closing_date',
            'occupancy',
            'hoa',
            'how_much',
            'payment_plan',
            'access',
            'date_aggreement',
            'agreement_document',
            'property_note',)