from django import forms
from django.contrib.auth.forms import (
    UserCreationForm, 
    AuthenticationForm, 
    UsernameField,
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm,)
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation
from components.models import Customer
class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Conform Password', widget=forms.PasswordInput())
    email = forms.EmailField(label='Email Address', required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True}))
    password = forms.CharField(label=_("Password"), strip=False, 
                widget=forms.PasswordInput(attrs={'autocomplete':'current-password'}))

class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete":"current-password", "autofocus":True}
        ),
    )
    new_password1 = forms.CharField(
        label=_("New Password"),
        strip=False,
        widget=(forms.PasswordInput(
            attrs={"autocomplete":"new-password"}
        )),
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("Conform new password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete":"new-password"}
        )
    )
class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete":"email"})
    )

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )
STATE_CHOICE = (
    ('Dhaka', 'Dhaka'),
    ('Khulna', 'Khulna'),
    ('Rajshahi', 'Rajshahi'),
    ('Chittagong', 'Chittagong'),
    ('Sylhet', 'Sylhet'),
    ('Barisal', 'Barisal'),
    ('Rangpur', 'Rangpur'),
)
# class CustomerForm(forms.Form):
#     name = forms.CharField(max_length=60, label="Name")
#     locality = forms.CharField(label="Locality")
#     city = forms.CharField(label="City")
#     zipcode = forms.IntegerField(label="ZipCode")
#     state = forms.ChoiceField(choices=STATE_CHOICE)

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["name", 'locality', 'city', 'zipcode', 'state']