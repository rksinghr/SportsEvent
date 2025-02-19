from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import raceMaster, athleteRegistration
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegSerializer
from .forms import AthRegForm
import requests

def home_view(request):
    eventList = raceMaster.objects.all()
    return render(request, 'app/home.html', {'eventList': eventList})

@login_required
def register_view(request, id):
    myRace = raceMaster.objects.filter(id = id).values()
    if request.method == "POST":
        for race in myRace:
            event_Name = race['name']
            event_ID = race['id']
            cat = request.POST['category']
            fname = request.POST["fName"]
            lname = request.POST["lName"]
            email = request.POST["email"]
            usrdob = request.POST["usrdob"]
            gender = request.POST["gender"]
            mob = request.POST["mob"]
            
            count = athleteRegistration.objects.filter(eventName=event_Name, gender=gender, eventCategory=cat).count()
            bib = (str(gender) + str(event_ID) + "-" + str(cat) + str(count + 1))

            data = {
                'firstName': fname,
                'lastName': lname,
                'dob': usrdob,
                'eventName': event_Name,
                'eventCategory': cat,
                'gender': gender,
                'email': email,
                'mob': mob,
                'bibNumber': bib,
                }
            
            # Define the URL of the external API
            api_url = "http://127.0.0.1:8000/RaceMate/createReg/"
            
            # Make the POST request
            response = requests.post(api_url, data=data)

            if response.status_code == 200:
                msg = "Registration Request successful, please check your email for more details."
                return render(request, 'app/success.html', {'page__message' : msg})

            else:
                # If the request fails, return the error
                msg = 'error: Request failed, status_code: ' + str(response.status_code)
                return render(request, 'app/success.html', {'page__message' : msg})

    return render(request, 'app/register.html', {'myRace' : myRace})

class RegCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the data to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def success_view(request):
    msg = "message"
    return render(request, 'app/success.html', {'page__message': msg})

@login_required
def reg_list_view(request):
    reg = athleteRegistration.objects.all()
    return render(request, 'app/reg_list.html', {'reg': reg})

@login_required
def edit_reg_view(request, pk):
    reg = get_object_or_404(athleteRegistration, pk=pk)
    if request.method == 'POST':
        form = AthRegForm(request.POST, instance=reg)
        if form.is_valid():
            form.save()
            return redirect('reg_list')  # Redirect to book list after update
    else:
        form = AthRegForm(instance=reg)
    return render(request, 'app/edit_reg.html', {'form': form, 'reg': reg})

@login_required
def delete_reg_view(request, pk):
    reg = get_object_or_404(athleteRegistration, pk=pk)
    if request.method == 'POST':
        reg.delete()
        return redirect('reg_list')  # Redirect to book list after deletion
    return render(request, 'app/del_reg.html', {'reg': reg})
