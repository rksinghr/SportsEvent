from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
import pyotp
from datetime import date, datetime
from .models import otpBank, UserProfile
from .utils import generate_otp, email_service, utc

def login_view(request):
    error_message=''
    if request.method == "POST":
        username = request.POST["usr"]
        otp, valid_time = generate_otp(username)
        subject_txt = 'OTP to login to RaceMate'
        msg_txt = 'Your one time password is: ' + str(otp) + ' - It is valid till: ' + str(valid_time)
        email_service(username, subject_txt, msg_txt)
        request.session['username'] = username
        return redirect ('racemateotp')
    return render(request, 'users/login.html', {'error_message': error_message})

def otp_view(request):
    error_message = None
    if request.method == 'POST':
        scrotp = request.POST['otp']
        username = request.session['username']
        otp_obj = otpBank.objects.filter(key_user = username).order_by('-otp_valid_date').first()
        osk = otp_obj.otp_secret_key
        otp_valid_date = otp_obj.otp_valid_date
        if osk and otp_valid_date is not None:
            valid_until = datetime.fromisoformat(str(otp_valid_date))
            tnow = datetime.now(utc)
            if valid_until > tnow:
                newhotp = pyotp.HOTP(osk)
                if newhotp.verify(scrotp, 1401):
                    # request.session['username'] = username
                    res = validate_user_view(request)
                    if res == 1:
                        return redirect('home')
                    else:
                        error_message = 'Oops!...Something went wrong during login, try again'
                else:
                    error_message = 'Invalid OTP'
            else:
                error_message = 'OTP Expired, request for new'
        else:
            error_message = 'Oops!...Something went wrong, try again'
    else:
        return render(request, 'users/otp.html', {'error_message':error_message})

@login_required
def changepwd_view(request):
    return render(request, 'users/change_pwd.html')

@login_required
def resetpwd_view(request):
    return render(request, 'users/reset_pwd.html')

@login_required
def usrprofile_view(request):
    if request.user.is_authenticated:
        obj, created = UserProfile.objects.get_or_create(
            user=request.user, eMail=request.user,
            defaults={"dob": date(1940, 1, 1)},)

        # form = ProfileForm(request.POST or None, instance=obj)
        if request.method == "POST":
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            dob = request.POST.get('dob')
            mob = request.POST.get('mob')
            altmob = request.POST.get('altmob')
            addl1 = request.POST.get('addl1')
            addl2 = request.POST.get('addl2')
            pin = request.POST.get('pin')
            state = request.POST.get('state')
            dist = request.POST.get('dist')
            city = request.POST.get('city')
            sch = request.POST.get('sch')
            acad = request.POST.get('acad')
            uid = request.POST.get('uid') 
            psport = request.POST.get('psport')
            height = request.POST.get('height')
            weight = request.POST.get('weight')
            print(dob)
            
            profile, created = UserProfile.objects.update_or_create(
            user_id=request.user.id,  # Assuming 'user_id' is unique and identifies the profile
            defaults={
                'firstName': fname, 'lastName': lname, 'dob': dob, 'mob': mob, 'altmob': altmob,
                'addl1': addl1, 'addl2': addl2, 'pin': pin,'state': state, 'dist': dist, 'city': city,
                'sch': sch, 'acad': acad, 'uid': uid, 'psport': psport, 'height': height, 'weight': weight
                }
            )

            return redirect('home')
        else:
            profile_rec = UserProfile.objects.filter(user_id = request.user).values()        
            context = {
                'profile_rec': profile_rec
            }           
            return render(request, 'users/profile.html', context)
    else:
        messages.success(request, "Login required!")
        return redirect('home')
    # return render(request, 'users/profile.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def validate_user_view(request):
    res = 2
    username = request.session['username']
    if User.objects.filter(email=username).exists():
        user = get_object_or_404(User, email=username)
        login(request, user)
        res = 1
    else:
        user = User.objects.create_user(username, username, username)
        error_message = 'User Created using OTP varification'
        login(request, user)
        res = 1
    return res