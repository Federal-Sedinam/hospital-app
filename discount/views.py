from django.shortcuts import render
from .form import appointment_form

def home(request):
    return render(request, 'home.html')

def appointment_confirmation(request):
    return render(request, 'appointment_confirmation.html')

def book_appointment(request):
    if request.method == 'POST':
        form = appointment_form(request.POST)
        if form.is_valid():
            total_cost = 0
            patient_name = form.cleaned_data["name"]
            service = form.cleaned_data["service"].lower()
            discount = form.cleaned_data["discount"].lower()
           
            services = {
                "dialysis": "880",
                "malaria": "750",
                "cholera": "660"     
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

