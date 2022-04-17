from django.urls import path

from inquiry import views

urlpatterns = [
    path('verify_mobile_number/', views.verify_mobile_number, name='verify_mobile_number'),
    path('enter_otp/', views.verify_otp, name='enter_otp'),
    path('inquiry/', views.inquiry, name='inquiry'),

]