from django.urls import path
from . import views

urlpatterns = [
    path('gen_cert/', views.generate_certificate, name='generate_certificate'),
]
