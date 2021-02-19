from django.http import *
from django.shortcuts import render
from django.conf import settings
from filebrowser.base import FileListing
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.cache import cache_control

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_passes_test(lambda user: user.is_anonymous, login_url='/home', redirect_field_name=None)
def login_user(request):
    try:
        user = authenticate(username = request.POST['username'],
            password = request.POST['password'])
    except KeyError:
        return render(request, 'registration/login.html')

    if user is not None:
        #'User' and 'Pass' right
        if user.is_active:
            login(request, user)
        else:
            return render(request, 'registration/login.html',{
                'login_message' : 'The user has been removed',})
    else:
        return render(request, 'registration/login.html',{
            'login_message' : 'Incorrect username or password!',})
    return HttpResponseRedirect('/home/')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(redirect_field_name='redir')
def home_view(request):
    filelisting = FileListing(settings.MEDIA_ROOT, sorting_by='date', sorting_order='desc')
    files = filelisting.listing()
    return render(request, 'index.html', {'files' : files})

@login_required(redirect_field_name='redir')
def home_alert(request, alert):
    filelisting = FileListing(settings.MEDIA_ROOT, sorting_by='date', sorting_order='desc')
    files = filelisting.listing()
    return render(request, 'index.html', {'files' : files, 'alert': alert})
