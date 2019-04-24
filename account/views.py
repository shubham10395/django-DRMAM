from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from account.models import labinfo,classinfo


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
        'name_of_os':obj.name_of_os,
        'ram':obj.ram,
        'starage':obj.starage

    }

    return render(request, 'account/all_labs/labs.html', context)

def labtwo(request):

    obj2 = labinfo.objects.get(id=2)
    context = {
        'lab_incharge':obj2.lab_incharge,
        'no_of_pc':obj2.no_of_pc,
        'name_of_os':obj2.name_of_os,
        'ram':obj2.ram,
        'starage':obj2.starage

    }

    return render(request, 'account/all_labs/labtwo.html', context)

def labthree(request):

    obj3 = labinfo.objects.get(id=3)
    context = {
        'lab_incharge':obj3.lab_incharge,
        'no_of_pc':obj3.no_of_pc,
        'name_of_os':obj3.name_of_os,
        'ram':obj3.ram,
        'starage':obj3.starage

    }

    return render(request, 'account/all_labs/labthree.html', context)

def labf(request):

    obj4 = labinfo.objects.get(id=4)
    context = {
        'lab_incharge':obj4.lab_incharge,
        'no_of_pc':obj4.no_of_pc,
        'name_of_os':obj4.name_of_os,
        'ram':obj4.ram,
        'starage':obj4.starage

    }

    return render(request, 'account/all_labs/labf.html', context)

def labfi(request):

    obj5 = labinfo.objects.get(id=5)
    context = {
        'lab_incharge':obj5.lab_incharge,
        'no_of_pc':obj5.no_of_pc,
        'name_of_os':obj5.name_of_os,
        'ram':obj5.ram,
        'starage':obj5.starage

    }

    return render(request, 'account/all_labs/labfi.html', context)

def labsi(request):

    obj6 = labinfo.objects.get(id=6)
    context = {
        'lab_incharge':obj6.lab_incharge,
        'no_of_pc':obj6.no_of_pc,
        'name_of_os':obj6.name_of_os,
        'ram':obj6.ram,
        'starage':obj6.starage

    }

    return render(request, 'account/all_labs/labsi.html', context)

def labse(request):

    obj7 = labinfo.objects.get(id=7)
    context = {
        'lab_incharge':obj7.lab_incharge,
        'no_of_pc':obj7.no_of_pc,
        'name_of_os':obj7.name_of_os,
        'ram':obj7.ram,
        'starage':obj7.starage

    }

    return render(request, 'account/all_labs/labse.html', context)



def classroom(request):

    obj = classinfo.objects.get(id=1)
    context = {
        'strength':obj.strength,
        'projector':obj.projector,
        'description':obj.description


    }

    return render(request,'account/classrooms/classroom_one.html', context)
