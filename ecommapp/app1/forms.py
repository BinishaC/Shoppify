from django import forms
from django.contrib.auth.models import User
from app1.models import Carts,Orders

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password','email']
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'first_name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'last_name'}),
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'UserName'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}),

        }

class UserLoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'username'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}),
        }

class CartForm(forms.ModelForm):
    class Meta:
        model=Carts
        fields=['quantity']
        widgets={
            'quantity':forms.NumberInput(attrs={'class':'form-control','placeholder':'quantity'}),
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model=Orders
        fields=['address','email']
        widgets={
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }

           