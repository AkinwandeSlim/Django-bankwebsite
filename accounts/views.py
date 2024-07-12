

import requests
import re
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
import random
import smtplib
from email.mime.text import MIMEText
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm,ProfileUpdateForm,CustomUserChangeForm
from .utils import *
from .models import Profile

# class SignUpView(CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy("login")
#     template_name = "registration/signup.html"





@csrf_exempt
def signup_view(request):
    if request.method == 'GET':
        return render(request, 'registration/signup.html')
    elif request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        if password != password_confirm:
            return JsonResponse({'error': 'Passwords do not match'}, status=400)

        otp = generate_otp()
        request.session['otp'] = otp
        request.session['user_data'] = {
            'username': username,
            'email': email,
            'password': password,
        }
        subject='Email Verification OTP'
        message = f'Your OTP is {otp}'
        send_otp_email(email, message,subject)
        return JsonResponse({'success': True})





@csrf_exempt
def verify_otp(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            otp = data['otp-input']
            if int(otp) == request.session.get('otp'):
                user_data = request.session.get('user_data')
                user_data['account_id']= generate_unique_account_id()
                user = get_user_model().objects.create_user(**user_data)
                # Usage
                user.save()
                del request.session['user_data']
                del request.session['otp']
                # Send account ID to user email
                subject='SVRB Account Info'
                send_otp_email(user_data['email'], f'Your account ID is {user.account_id}',subject)
                # return JsonResponse({'success': True})
                                # Redirect to the login page
                # Redirect to the login page
                return JsonResponse({'success': True, 'redirect_url': '/accounts/login/'})

            else:
                return JsonResponse({'error': 'Invalid OTP'}, status=400)
        except (KeyError, ValueError) as e:
            return JsonResponse({'error': 'Invalid request'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid method'}, status=405)




# @csrf_exempt
# def login_view(request):
#     if request.method == 'POST':
#         username_or_account_id = request.POST['username_or_account_id']
#         password = request.POST['password']
#         user = authenticate(request, username=username_or_account_id, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             return render(request, 'registration/login.html', {'error': 'Invalid login credentials'})
#     return render(request, 'registration/login.html')




@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Invalid username or password'})
    else:
        return render(request, 'registration.html')

# @csrf_exempt
# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username_or_account_id')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return JsonResponse({'success': True, 'message': 'Authenticated successfully'})
#         else:
#             return JsonResponse({'success': False, 'message': 'Invalid credentials'})
#     return JsonResponse({'success': False, 'message': 'Invalid request method'})

@login_required
def loans(request):
    return render(request, 'loans.html', {'title': 'Loans'})



def logout_view(request):
    logout(request)
    return redirect('login')



@login_required
def profile(request):
    if request.method == 'POST':
        user_profile, created = Profile.objects.get_or_create(user=request.user)
        
        u_form = CustomUserChangeForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = CustomUserChangeForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)



    # Retrieve the account balance
    account_balance = request.user.profile.account_balance
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'account_balance': account_balance,
        'title': 'Profies',
    }

    return render(request, 'profile_update.html', context)





# @login_required
# def update_profile(request):
#     if request.method == 'POST':
#         form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')
#     else:
#         form = ProfileUpdateForm(instance=request.user.profile)
#     return render(request, 'profile_update.html', {'form': form})



@login_required
def deposit(request):
    if request.method == 'POST':
        amount = float(request.POST.get('amount'))
        profile = request.user.profile
        profile.account_balance += amount
        profile.save()
        return JsonResponse({'success': True, 'new_balance': profile.account_balance})
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)




# @login_required
# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from .models import Account  # Assuming you have an Account model

@login_required
def withdraw(request):
    if request.method == 'POST':
        amount = request.POST['amount']
        profile = request.user.profile
        # profile.account_balance += amount
        if  profile.account_balance >= float(amount):
            profile.account_balance -= float(amount)
            return JsonResponse({'success': True, 'new_balance': profile.account_balance})
        else:
            return JsonResponse({'success': False, 'error': 'Insufficient funds'})

