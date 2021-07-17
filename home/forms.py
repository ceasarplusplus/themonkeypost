from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from store.models import Product
from order.models import Order
from django.forms import TextInput, EmailInput, Select, FileInput
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import Userprofile


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)


PAYMENT_CHOICES = (
    ('B', 'Bank Transfer'),
    ('C', 'Credit Card'),


)


class OrderForm(forms.ModelForm):

    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES)

    class Meta:
        model = Order
        fields = ['first_name', 'last_name',
                  'address', 'phone', 'city', 'state', 'payment_option']


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, label='User Name :')
    email = forms.EmailField(max_length=200, label='Email :')
    first_name = forms.CharField(
        max_length=100, label='First Name :')
    last_name = forms.CharField(
        max_length=100, label='Last Name :')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'password1', 'password2', )
        widgets = {
            'username': TextInput(attrs={'class': 'input form-control', 'placeholder': 'username', 'name': 'username'}),
            'email': EmailInput(attrs={'class': 'input form-control', 'placeholder': 'Enter your Email', 'name': 'email'}),
            'password1': TextInput(attrs={'class': 'input form-control', 'placeholder': 'Password', 'name': 'password1'}),
            'password2': TextInput(attrs={'class': 'input form-control', 'placeholder': 'Confirm Password', 'name': 'password2'}),
            # 'image': FileInput(attrs={'class': 'input form-control', 'placeholder': 'image', }),
        }


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        widgets = {
            'username': TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'first_name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'last_name'}),
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Userprofile
        fields = ('phone', 'address', 'city', 'state', 'image')
        widgets = {
            'phone': TextInput(attrs={'class': 'form-control', 'placeholder': 'phone'}),
            'address': TextInput(attrs={'class': 'form-control', 'placeholder': 'address'}),
            'city': TextInput(attrs={'class': 'form-control', 'placeholder': 'city'}),
            'state': TextInput(attrs={'class': 'form-control', 'placeholder': 'state'}),
            # 'image': FileInput(attrs={'class': 'input form-control', }),
        }
