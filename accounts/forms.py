# accounts/forms.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import models
from .models import CustomUser
from django import forms
from .models import Profile
class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = (
                "username",
                "email",
                "password1",
                "password2",
            )


class CustomUserChangeForm(UserChangeForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'type': 'email',
                'id': 'input-email',
                'class': 'form-control form-control-alternative',
                'placeholder': 'youremail@example.com'
            }
        )
    )


    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'id': 'input-username',
                'class': 'form-control form-control-alternative',
                'placeholder': 'Username'
            }
        )
    )


    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'id': 'input-first_name',
                'class': 'form-control form-control-alternative',
                'placeholder': 'first_name'
            }
        )
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'id': 'input-last_name',
                'class': 'form-control form-control-alternative',
                'placeholder': 'last_name'
            }
        )
    )
    class Meta:
        model = CustomUser
        # fields = ("username", "email", "account_id")
        fields = ['first_name', 'last_name','username','email']






class ProfileUpdateForm(forms.ModelForm):
    phone = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                'type': 'number',
                'id': 'input-phone',
                'class': 'form-control form-control-alternative',
                'placeholder': '+1234567890'
            }
        )
    )



    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'id': 'input-address',
                'class': 'form-control form-control-alternative',
                'placeholder': 'address'
            }
        )
    )





    city = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'id': 'input-city',
                'class': 'form-control form-control-alternative',
                'placeholder': 'city'
            }
        )
    )


    country = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'id': 'input-country',
                'class': 'form-control form-control-alternative',
                'placeholder': 'country'
            }
        )
    )


    postal_code = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                'type': 'number',
                'id': 'input-postal_code',
                'class': 'form-control form-control-alternative',
                'placeholder': 'Postal code'
            }
        )
    )

    class Meta:
        model = Profile
        fields = ['phone', 'image', 'address', 'city', 'country', 'postal_code','account_balance']



        widgets = {
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control form-control-alternative d-none',
                'id': 'imgInp',
            }),
        }