from django.urls import path
from . import views

from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView



urlpatterns = [
        path('login',
auth_views.LoginView.as_view(template_name='user_auth/login.html'),
             name='login'),
        path('logout',
             auth_views.LogoutView.as_view(next_page="/"),
             name='logout'),
        path('register',
             views.register,
             name="register"),
        path('profiles',
             views.profiles,
             name="profiles"),
        path('profiles/<int:id>',
             views.profile_test,
             name="profile"),
]
