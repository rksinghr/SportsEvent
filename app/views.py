from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import raceMaster, athleteRegistration
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegSerializer
import requests

def home_view(request):
    eventList = raceMaster.objects.all().values()
    return render(request, 'app/home.html', {'eventList': eventList})

@login_required
def register_view(request, id):
    myRace = raceMaster.objects.filter(id = id).values()
    if request.method == "POST":
        for race in myRace:
            event_Name = race['name']
            event_ID = race['id']
            fname = request.POST["fName"]
            lname = request.POST["lName"]
            email = request.POST["email"]
            usrdob = request.POST["usrdob"]
            gender = request.POST["gender"]
            mob = request.POST["mob"]

            data = {
                'firstName': fname,
                'lastName': lname,
                'dob': usrdob,
                'eventName': event_Name,
                'gender': gender,
                'email': email,
                'mob': mob,
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
