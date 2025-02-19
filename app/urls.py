from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('register/<int:id>', views.register_view, name='register'),
    path('createReg/', views.RegCreateAPIView.as_view(), name='createReg'),
    path('regList', views.reg_list_view, name='reg_list'),
    path('editReg/<int:pk>/', views.edit_reg_view, name='edit_reg'),
    path('deleteReg/<int:pk>/', views.delete_reg_view, name='delete_reg'),
    # path('generate_qr/<str:data>/', generate_qr_code, name='generate_qr_code'),
    # path('success/', views.success_view, name='success'),
]