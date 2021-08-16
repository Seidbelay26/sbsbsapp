from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Meetme, Participants
from .forms import RegistrationForm
# Create your views here.
def home(request):
    meetme=Meetme.objects.all()
    return render(request, 'meetme/home.html', {'meetme': meetme})

def meetme_details(request, meetme_slug):
    try:
        selected_meetme = Meetme.objects.get(slug=meetme_slug)
        if request.method == 'GET':            
            registration_form = RegistrationForm()
        else:
            registration_form=RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email = registration_form.cleaned_data['email']
                user_name = registration_form.cleaned_data['name']
                participant, _ = Participants.objects.get_or_create(email=user_email)
                return redirect('confirm-registration', meetme_slug=meetme_slug)
        return render(request,'meetme/meetme-details.html', {'meetme_found': True,'meetme':selected_meetme,'form': registration_form })

    except Exception as exc:
        print(exc)
        return render(request,'meetme/meetme-details.html', {'meetme_found': False})


def confirm_registration(request, meetme_slug):
    meetme=Meetme.objects.get(slug=meetme_slug)
    return render(request,'meetme/registration-success.html',{
        'organizer_email': meetme.organizer_email
    })

