from django.shortcuts import render, redirect
from .form import UserRegisterForm, CustomerForm
from django.views import View
from django.contrib import messages
from components.models import Customer
from django.contrib.auth.decorators import login_required 
from django.utils.decorators import method_decorator
# Create your views here.

class UserRegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        context = {
            'form' : form,
        }
        return render(request, 'auth/register.html', context)
    
    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() 
        context = {
            'form':form,
        }
        return redirect('/user/profile/')
    

@method_decorator(login_required, name="dispatch")
class CustomerProfileView(View):
    def get(self, request):
        form = CustomerForm()
        context = {'form':form}
        return render(request, 'auth/address.html', context)
    
    def post(self, request):
        form = CustomerForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            zipcode = form.cleaned_data['zipcode']
            state = form.cleaned_data['state']
            reg = Customer(user=user, name=name, locality=locality, city=city, zipcode=zipcode, state=state)
            reg.save()
            messages.success(request, "Congratulation! Profile Updated Successfully")
        return render(request, 'auth/address.html', {'form':form})


@method_decorator(login_required, name="dispatch")
class UserProfileView(View):
    def get(self, request):
        user = Customer.objects.filter(user = request.user)
        context = {
            'user':user
        }
        return render(request, 'auth/profile.html', context)