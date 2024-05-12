"""
URL configuration for Beauty_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from App_beauty import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('admin/',admin.site.urls),
    path('About/', views.About, name='About'),
    path('Gallery/', views.Gallery, name='Gallery'),
    path('Location/', views.Location, name='Location'),
    path('Services/', views.Services, name='Services'),
    path('beauty_com/',views.beauty_com,name='beauty_com'),
    path('customer_photos/', views.customer_photos, name='customer_photos'),
    path('hair/', views.hair, name='hair'),
    path('skin/', views.skin, name='skin'),
    path('makeup/', views.makeup, name='makeup'),
    path('book_appointment/', views.book_appointment, name='book_appointment'),
    path('cut_all/', views.cut_all, name='cut_all'),
    path('hair_treatment/', views.hair_treatment, name='hair_treatment'),
    path('hair_color/', views.hair_color, name='hair_color'),
    path('signin/', views.signin, name='signin'),
    path('signup/',views.signup, name='signup'),
    path('appointment_confirmation/', views.appointment_confirmation,name='appointment_confirmation'),
    path('feedback/', views.feedback,name='feedback'),
    path('reviews/', views.showfeedback, name='reviews'),
    path('signout/', views.signout, name='signout'),
    path('thank_you/', views.thank_you,name='thank_you')

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#print(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
