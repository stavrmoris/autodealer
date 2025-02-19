from django.urls import path
from . import views

urlpatterns = [
    path('form1/', views.feedback1, name='feedback1'),
    path('form2/', views.feedback2, name='feedback2'),
]