from django.contrib import admin
from django.urls import path
# import settings and static from django.conf 
# in other to set the media root and static url
from django.conf import settings
from django.conf.urls.static import static
from app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('property/', views.ListProperty.as_view(), name="property"),
    path('property_detail/<slug:slug>', views.property_detail, name="property_detail"),
    path('offer', views.become_a_buyer, name="become_a_buyer"),
    path('jv-form', views.jv, name="jvform"),
    path('privacy-policy', views.privacy_policy, name="privacy-policy"),
    path('terms', views.terms_and_conditions, name="terms"),
    path('about', views.about, name="about"),
    path('register', views.register, name="register"),
    path('profile', views.edit_form, name="profile"),
    path('login/', auth_views.LoginView.as_view(template_name= 'app/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name= 'app/index.html'), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)