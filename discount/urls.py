from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bookappointment/', views.book_appointment, name='bookappointment'),
    path('bookappointment/<int:appointment_id>', views.book_appointment, name='bookappointment'),
    path('appointment_confirmation', views.appointment_confirmation, name='confirmation')
]
