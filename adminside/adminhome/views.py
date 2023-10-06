from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def adminlogin(request):
    if 'username' in request.session:
        return redirect('adminhome')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        
        
        if user is not None and user.is_superuser:
            login(request, user)
            request.session['username'] = username
            return redirect('adminhome')
        else:
            messages.info(request, 'Invalid username or password. Please try again.')
            return redirect('adminlogin')
    else:
        error_message = ""

    return render(request, 'adminlogin.html')




def adminhome(request):
    return render(request,'adminhome.html')

def adminlogout(request):
    if 'username' in request.session:
        request.session.flush()
        return redirect('adminlogin') 
    return render(request,'adminlogin.html')

def admin_change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Update the session with the new password hash
            messages.success(request, 'Your password was successfully updated.')
            return redirect('adminhome')
        else:
            messages.error(request, 'Please correct the error(s) below.')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'profile.html', {'form': form})




