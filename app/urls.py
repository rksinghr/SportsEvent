from django.urls import path
from .views import RegCreateAPIView, home_view, register_view
urlpatterns = [
    path('home/', home_view, name='home'),
    path('register/<int:id>', register_view, name='register'),
    path('createReg/', RegCreateAPIView.as_view(), name='createReg'),
    # path('success/', views.success_view, name='success'),
]