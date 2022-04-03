
from django import views
from django.contrib import admin
from django.urls import path,include
from.views import UserRegister ,UserEditView ,PasswordsChangeView ,ShowProfilePageView  ,EditProfilePageView ,CreateProfilePageView
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
  path('register/' ,UserRegister.as_view() ,name="register"),
  path('edit_profile/' ,UserEditView.as_view() ,name="edit-profile"),
  #path('password/' ,auth_views.PasswordChangeView.as_view(template_name= 'registration/change_password.html')),
  path('password/' ,PasswordsChangeView.as_view(template_name= 'registration/change_password.html')),
  path('password_success/' ,views.password_success , name ='password_success'),
  path('<int:pk>/profile/' , ShowProfilePageView.as_view() , name="show-profile-page"),
  path('<int:pk>/edit_profile/' , EditProfilePageView.as_view() , name="edit-profile-page"),
  path('create_profile_page/' , CreateProfilePageView.as_view() , name="create-profile-page"),

  
]

