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

            return redirect('login')

    return render(request,'registration/register.html',{'form':form})