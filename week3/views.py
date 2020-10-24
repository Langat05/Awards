from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, 'index.html', locals())

def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    context = {
        'form':form,
    }
    return render(request, 'registration/register.html', context)