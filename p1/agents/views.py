from django.shortcuts import render ,redirect
from django.http import Http404,HttpResponse,JsonResponse
from .forms import CreateAgentsForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User



@login_required(login_url='login')
def homePage(request):
    form = CreateAgentsForm()
    all_users = User.objects.values()
    print(all_users)
    print(all_users[0]['username'])
    return render(request , 'agents/home.html',{'form' : form , 'userlist' : list})

@login_required(login_url='login')
def logoutPage(request):
    logout(request=request)
    return redirect('login')



def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request , username = username , password = password)
        if user is not None:
            login(request,  user)
            return redirect('home') 
        else :
            messages.info(request,'Username or Password Invalid')
            # return render(request , 'client/login.html')        
        
    return render(request , 'agents/login.html')


