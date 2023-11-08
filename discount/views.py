from django.shortcuts import render, redirect
from .form import appointment_form

def home(request):
    return render(request, 'home.html')

def book_appointment(request):
    if request.method == 'POST':
        form = appointment_form(request.POST)
        if form.is_valid():
            total_cost = 0
            patient_name = form.cleaned_data["name"]
            service = form.cleaned_data["service"]
            discount = form.cleaned_data["discount"]

            services = {
                "Dialysis": "880",
                "Malaria": "750",
                "Cholera": "660"     
                        }
            
            if service in services:
                total_cost = services[service]
                if discount == ["pyclub", "python", "django"]:
                    total_cost *= 0.3

            form.save()
            return render(request, "appointment_confirmation.html", {"patient_name" : patient_name, "total_cost" : total_cost})
    else:
        form = appointment_form()

    return render(request, 'bookappointment.html', {'form': form})


    
    # total_cost = hospital_dict[service]
    # if discount_code == 'pyclubs':
    #     total_cost *= 0.3
    # elif discount_code == 'python':
    #     total_cost *= 0.4
    # elif discount_code == 'django':
    #     total_cost *= 0.6
    # Appointment.append({'name': name, 'service': service, 'total_cost': total_cost})
    # return f'Appointment booked for {name}. Total cost is GHC {total_cost} '
    

# def display_appointment():
#     if not Appointment:
#         return 'No appointment booked'
#     else:
#         return Appointment
    
# print(book_appointment())
# print(book_appointment())
# print(display_appointment())
