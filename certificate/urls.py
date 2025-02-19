from django.urls import path
from . import views

urlpatterns = [
    path('certificate/', views.certificate_view, name='certificate'),
]
