from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout


def Home(request):

    return render(request,'account/home.html')

def login(request):
    username = request.POST.get['username']
    password = request.POST.get['password']
    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)
        return render(request,'account/profile.html')

        # Redirect to a success page.
        ...
    else:
        return render(request,'account/login.html')

        # Return an 'invalid login' error message.
        ...


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
