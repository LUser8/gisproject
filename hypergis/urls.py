from django.urls import path
from .views import home, flight_upload, register_field

urlpatterns = [
    path('', home, name='user-home'),
    path('field/register', register_field, name='register-field'),
    path('flight', flight_upload, name='flight-upload'),

]