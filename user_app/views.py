from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'
    
    
def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)   
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html',context={'form':form})