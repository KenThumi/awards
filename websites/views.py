from websites.email import send_welcome_email
from websites.forms import UserRegisterForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def home(request):



    return render(request,'index.html')



def register(request):
    form = UserRegisterForm()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()

            send_welcome_email(form.cleaned_data['username'], form.cleaned_data['email'])

            return redirect('login')

    return render(request,'registration/register.html',{'form':form})