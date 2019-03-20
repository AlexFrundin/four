from django.shortcuts import (render,
                              HttpResponse,
                              redirect,
                              get_object_or_404,
                              Http404)
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm, User as fUser
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .forms import FormProfile, FormUser
from .models import Profile


# Create your views here.

def register(request):
    context = {}
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=User.objects.create_user(username=username,
                                              password=password)
            login(request, authenticate(username=username,
                                        password=password))
            return redirect("profile",id=user.id)
    context['user_form'] = form
    return render(request, 'user_auth/register.html',context)

@login_required(login_url="login")
def profiles(request):
    id = request.session['_auth_user_id']
    username = request.user
    #user = User.objects.filter(username=request.user)[0]
    #user = User.objects.get(id=id)
    # user = User.objects.get(username=username)
    user = get_object_or_404(User, username=username)
    print(user)
    return HttpResponse('Profiles')

@login_required(login_url="login")
def profile_test___old(request,id):
    user = User.objects.get(id=id)
    user_form = FormUser(instance=user)
    try:
        profile = Profile.objects.get(user = user)
    except:
        profile = None
    profile_form = FormProfile(instance=profile)
    if request.method == "POST":
        user_form = FormUser(request.POST, instance=user)
        profile_form = FormProfile(request.POST,instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            birth = profile_form.cleaned_data['birth']
            gender = profile_form.cleaned_data['gender']
            telephone = profile_form.cleaned_data['telephone']
            try:
                p = Profile(user=user, birth=birth,gender=gender,telephone=telephone)
                p.save()
            except:
                profile_form.save()
    context = {}
    context['user_form'] = user_form
    context['profile_form'] = profile_form
    return render(request, "profile/profiles.html", context)

@login_required(login_url="login")
def profile_test(request,id):
    if request.user.id != id:
        raise Http404("Your failed id")
    # user = User.objects.get(id=id)
    user_form = FormUser(instance=request.user)
    try:
        profile = request.user.profile
    except:
        profile = Profile.objects.create(user=request.user)
    profile_form = FormProfile(instance=profile)

    if request.method == "POST":
        user_form = FormUser(request.POST,instance=request.user)
        profile_form = FormProfile(request.POST,instance=profile, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            profile = request.user.profile
            print(dir(request.user))
            profile.get_image()
            return HttpResponse("Your data save!")
    context = {}
    context['user_form'] = user_form
    context['profile_form'] = profile_form
    return render(request, "profile/profiles.html", context)
