from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField


STATUS = (
        ("Available", "Available"),
        ("Pending", "Pending"),
        ("Sold", "Sold")
    )
PARKING =(
        ("Driveway", "Driveway"),
    )
OPTION = (
        ("YES", "YES"),
        ("NO", "NO"),
    ) 
PAYMENT_PLAN = (
    ("MONTHLY", "MONTHLY"),
    ("QUATERLY", "QUATERLY"),
    ("ANNUALLY", "ANNUALLY")
)  
class PropertyType(models.Model):
    property_name = models.CharField(max_length = 150, verbose_name = 'Category name')
    description = models.TextField(verbose_name = 'Description', blank = True, null = True)
    def __str__(self):
        return self.property_name

# Create your models here.
class Property(models.Model):
    title = models.CharField(max_length =150, verbose_name = 'Property Title')
    slug = models.SlugField(max_length=200, unique=True, blank = True, null = True)
    property_category = models.ForeignKey(PropertyType, on_delete = models.CASCADE, verbose_name = 'Post Category')
    img = models.ImageField(verbose_name = 'Property Featured Image')
    floor_plan = models.ImageField(verbose_name= 'Floor Plan')
    description = models.TextField(verbose_name = 'Post Contents')
    price = models.IntegerField()
    arv = models.IntegerField(blank = True, null = True)
    gross_margin = models.IntegerField(blank = True, null = True)
    year_build = models.IntegerField()
    parking = models.CharField(max_length=30, choices=PARKING, default="Driveway")
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    sq_footage = models.CharField(max_length=100)
    lot_size = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS, default="Available")
    video = models.URLField(max_length=500, blank = True, null = True, verbose_name="Link to video(vimeo)")
    class Meta:
        ordering  = ['-created_date']
    def __str__(self):
        return self.title

# create a model for offer
class Offer(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='offers')
    email = models.EmailField(verbose_name = "Email Address")
    name = models.CharField(max_length = 150,)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Offer {} by {}'.format(self.message, self.name)

class Testimonial(models.Model):
    testimonial_name = models.CharField(max_length = 150, verbose_name = 'Testimonial Name')
    testimonial_img = models.ImageField(verbose_name = 'Testimonial Image')
    testimonial_contents = models.TextField(verbose_name = 'Testimonial Contents')
    def __str__(self):
        return self.testimonial_name

class Contact(models.Model):
    name = models.CharField(max_length =150, verbose_name ="Name")
    email = models.EmailField(max_length = 150, verbose_name = "Email Address")
    subject = models.CharField(max_length = 150, verbose_name = "Subject")
    message = models.TextField(verbose_name = "Contact Message")
    def __str__(self):
        return self.name

class JointVenture(models.Model):
    first_name = models.CharField(max_length =150, verbose_name ="First Name")
    last_name = models.CharField(max_length =150, verbose_name ="Last Name")
    email = models.EmailField(max_length = 150, verbose_name = "Email Address")
    phone = PhoneField(blank=True, help_text='Contact phone number')
    company_name = models.CharField(max_length =150, verbose_name ="Company Name")
    property_address = models.CharField(max_length =150, verbose_name ="Property Address")
    sq_footage = models.CharField(max_length=100)
    acquisition_price = models.IntegerField()
    asking_price = models.IntegerField()
    arv = models.IntegerField(blank = True, null = True)
    year_build = models.IntegerField()
    year_roof = models.IntegerField()
    year_hvac = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    comp1_link = models.URLField(max_length=200)
    comp1_price = models.IntegerField()
    comp2_link = models.URLField(max_length=200, blank = True, null = True)
    comp2_price = models.IntegerField(blank = True, null = True)
    comp3_link = models.URLField(max_length=200, blank = True, null = True)
    comp3_price = models.IntegerField(blank = True, null = True)
    photo_link = models.URLField(max_length=500)
    inspection_date = models.DateTimeField()
    closing_date = models.DateTimeField()
    occupancy = models.CharField(max_length=200)
    hoa = models.CharField(choices=OPTION, max_length=3, blank = True, null = True)
    how_much = models.CharField(max_length=200, blank = True, null = True)
    payment_plan = models.CharField(choices=PAYMENT_PLAN, max_length=8, blank = True, null = True)
    access = models.CharField(max_length=200)
    date_aggreement = models.DateTimeField()
    agreement_document = models.FileField(upload_to='documents/', verbose_name = 'Original Purchase Agreement')
    property_note = models.TextField(blank = True, null = True)
    created_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering  = ['-created_date']
    def __str__(self):
        return self.first_name


class BecomeBuyer(models.Model):
    first_name = models.CharField(max_length =150, verbose_name ="First Name")
    last_name = models.CharField(max_length =150, verbose_name ="Last Name")
    email = models.EmailField(max_length = 150, verbose_name = "Email Address")
    phone = PhoneField(blank=True, help_text='Contact phone number')
    company_name = models.CharField(max_length =150, verbose_name ="Company Name")
    area_buying = models.CharField(max_length=200)
    property_address = models.CharField(max_length =150, verbose_name ="Property Address", blank = True, null = True)
    note = models.TextField(blank = True, null = True)
    created_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering  = ['-created_date']
    def __str__(self):
        return self.first_name