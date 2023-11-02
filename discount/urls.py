from django.urls import path
from . import views

urlpatterns = [
    # path('bookappointment/', views.book_appointment, name='bookappointment'),
    path('', views.home, name='home'),
    path('bookappointment/', views.book_appointment, name='bookappointment')
]
