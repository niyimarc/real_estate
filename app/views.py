from django.shortcuts import render, get_object_or_404
from .models import Property, Testimonial, User
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.http import HttpResponseRedirect
from app.forms import ContactForm, OfferForm, BecomeBuyerForm, JointVentureForm
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    property = Property.objects.all()
    testitomy = Testimonial.objects.all()
    current_user = request.user
    return render(request, "app/index.html", {
                                                "property": property, 
                                                "testimonial": testitomy,
                                                'navbar': 'home',
                                                'current_user': current_user,
                                                })
def contact(request):
    current_user = request.user
    if request.method == "POST":
        contactform = ContactForm(request.POST)
        if contactform.is_valid():
            contactform.save(commit=True)
            messages.success(request, "Message successfully submitted!")
            return HttpResponseRedirect('/contact')
        else:
            messages.error(request, "Message not submitted! Please fill out all fields correctly")
    else:
        contactform = ContactForm()
    return render(request, "app/contact.html", {'navbar': 'contact', 'current_user': current_user})

class ListProperty(ListView):
    model = Property
    queryset = Property.objects.all().order_by('-created_date')
    template_name = 'app/property.html'
    context_object_name = 'list_properties'
    # def get(self, request, context_object_name):
    #     return render(request, "app/property.html", {'navbar': 'property', 'current_user': self.request.user, })

# the post_detail view will display the post based on the id of the post 
def property_detail(request, slug):
    template_name = 'app/detail_property.html'
    property = get_object_or_404(Property, slug=slug)
    current_user = request.user
 
    if request.method == 'POST':
        offer_form = OfferForm(data=request.POST)
        if offer_form.is_valid():  
            new_offer = offer_form.save(commit=False)  
            new_offer.property = property
            print(new_offer)
            new_offer.save()       
            messages.success(request, "Offer successfully submitted!")
            return HttpResponseRedirect('/property_detail/' + property.slug )
        else:
            messages.error(request, "Offer not submitted.")         
    else:
        offer_form = OfferForm()
    
    return render(request, template_name, {'property': property,
                                           'current_user': current_user,
                                           'offer_form': offer_form})
    
    
def become_a_buyer(request):
    current_user = request.user
    if request.method == "POST":
        becomebuyerform = BecomeBuyerForm(request.POST)
        if becomebuyerform.is_valid():
            becomebuyerform.save(commit=True)
            messages.success(request, "Message successfully submitted!")
            return HttpResponseRedirect('/offer')
        else:
            messages.error(request, "Message not submitted! Please fill out all fields correctly")
    else:
        becomebuyerform = BecomeBuyerForm()
    return render(request, "app/become_a_buyer.html", {'navbar': 'send_offer', 'current_user': current_user})

def jv(request):
    current_user = request.user
    if request.method == "POST":
        jointventureform = JointVentureForm(request.POST, request.FILES)
        if jointventureform.is_valid():
            jointventureform.save(commit=True)
            messages.success(request, "Message successfully submitted!")
            return HttpResponseRedirect('/jv-form')
        else:
            messages.error(request, "Message not submitted! Please fill out all fields correctly")
    else:
        jointventureform = JointVentureForm()
    return render(request, "app/jv.html", {'navbar': 'jvform', 'current_user': current_user})

def privacy_policy(request):
    current_user = request.user
    return render(request, "app/privacy.html", {'current_user': current_user}) 
def terms_and_conditions(request):
    current_user = request.user
    return render(request, "app/terms_and_conditions.html", {'current_user': current_user}) 
def about(request):
    current_user = request.user
    return render(request, "app/about.html", {'current_user': current_user}) 