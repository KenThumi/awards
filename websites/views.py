from websites.models import Profile, Project
from django.contrib import messages
from websites.email import send_welcome_email
from websites.forms import ProfileForm, ProjectForm, UserRegisterForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
import cloudinary.uploader


@login_required
def home(request):
    projects = Project.objects.all()

    ctx = {'projects':projects}

    return render(request,'index.html', ctx)



def register(request):
    form = UserRegisterForm()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()

            send_welcome_email(form.cleaned_data['username'], form.cleaned_data['email'])

            messages.success(request, 'Successful Registration.')

            return redirect('login')

    return render(request,'registration/register.html',{'form':form})


@login_required
def profile(request):
    user = request.user

    return render(request,'profile/profile.html', {'user':user})


@login_required
def addprof(request,id):
    form = ProfileForm()

    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)

        file_to_upload = request.FILES['profile_photo']

        if form.is_valid():
            upload_result = cloudinary.uploader.upload(file_to_upload)
            new_result = remove_prefix(upload_result['secure_url'],'https://res.cloudinary.com/dtw9t2dom/')

            profile = Profile(profile_photo=new_result,
                              bio=form.cleaned_data['bio'],
                              user=request.user)

            profile.save_profile()

            messages.success(request, 'Successful profile creation.')
            return redirect('profile')

    ctx = {'form':form}

    return render(request,'profile/update.html',ctx)



def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text

@login_required
def addProject(request):
    form = ProjectForm()
    if request.method=='POST':
        form = ProjectForm(request.POST,request.FILES)

        file_to_upload = request.FILES['image']
      
        if form.is_valid():
            upload_result = cloudinary.uploader.upload(file_to_upload)
            new_result = remove_prefix(upload_result['secure_url'],'https://res.cloudinary.com/dtw9t2dom/')

            project = Project(image=new_result,
                          title=form.cleaned_data['title'],
                          description=form.cleaned_data['description'],
                          link=form.cleaned_data['link'],
                          user=request.user,)

            project.save_project()

            messages.success(request, 'Successful upload.')
            return redirect('home')

    return render(request, 'addproject.html', {'form':form})

@login_required
def project(request,id):
    project = Project.objects.get(pk=id)


    return render(request,'project.html',{'project':project})