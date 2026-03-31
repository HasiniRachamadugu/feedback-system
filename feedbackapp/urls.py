from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('feedback/', views.feedback_form, name='feedback_form'),
    path('list/', views.feedback_list, name='feedback_list'),
    path('delete/<int:id>/', views.delete_feedback, name='delete_feedback'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

]