# from django.shortcuts import render, redirect
# from .models import appointment
# from .form import appointment_form


# def book_appointment(request):
#     if service not in hospital_dict:
#         return 'Service not available'
    
#     total_cost = hospital_dict[service]
#     if discount_code == 'pyclubs':
#         total_cost *= 0.3
#     elif discount_code == 'python':
#         total_cost *= 0.4
#     elif discount_code == 'django':
#         total_cost *= 0.6
#     Appointment.append({'name': name, 'service': service, 'total_cost': total_cost})
#     return f'Appointment booked for {name}. Total cost is GHC {total_cost} '
    

# def display_appointment():
#     if not Appointment:
#         return 'No appointment booked'
#     else:
#         return Appointment
    
# print(book_appointment())
# print(book_appointment())
# print(display_appointment())
