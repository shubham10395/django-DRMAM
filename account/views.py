from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from account.models import labinfo


def Home(request):

    return render(request,'account/home.html')


def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')
    else:
        form = UserCreationForm()
        args = {'form': form}
        return render(request, 'account/Signup.html', args)


def profile(request):

    return render(request,'account/profile.html')

def lab(request):

    obj = labinfo.objects.get(id=1)
    context = {
        'lab_incharge':obj.lab_incharge,
        'no_of_pc':obj.no_of_pc,
        'name_of_os':obj.name_of_os

    }





#    args = {'user': request.user}
    return render(request, 'account/labs.html', context)
