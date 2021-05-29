from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/login.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('addprofile/<int:id>', views.addprof, name='addprofile'),
    path('addproject/',views.addProject,name='addproject'),
    path('project/<int:id>', views.project, name='project'),
    path('addreview/<int:id>',views.addreview, name='addreview')
]
