from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password

from adminapp.models import AdminSetting, Meeting, User
from  adminapp.models import professions

def user_logout(request):
    logout(request)
    # Redirect to a success page, or wherever you want the user to go after logout
    return redirect('/login') 


def register(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')


    if request.method == 'POST':
        user = User.objects.create(
        email=  request.POST.get('email'),
        username = request.POST.get('username'),
        password = make_password(request.POST.get('password')),
        church_branch = request.POST.get('church_branch')
        )
        user.save()
        return user_login(request, username =request.POST.get('username'), password= request.POST.get('password'))   
        
    # Redirect to a success page, or wherever you want the user to go after logout
    return render(request,'auth/register.html') 


def user_login(request, username =None, password= None):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')  
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/dashboard')  # Replace '/dashboard' with the URL you want to redirect to after successful login
            else:
                # Return a disabled account error message
                context = {'message': 'Your account is disabled.'}
                return render(request, 'auth/login.html', context)
        else:
            # Return an invalid login error message
            context = {'message': f'Invalid username or password.'}
            return render(request, 'auth/login.html', context)

    # If request method is not POST, render the login form again without any message
    return render(request, 'auth/login.html')


@login_required
def dashboard(request):
    if not request.user.phonenumber and not request.user.location:
        message ="Please Complete your Profile Registration"
        return profile(request, message)
    
    setting,_ = AdminSetting.objects.get_or_create(pk =1)
    meetings = Meeting.objects.filter(is_meeting_done= True)
    attended_meeting = Meeting.objects.filter(
        is_meeting_done= True, attendees = request.user).count() or 0
    
    

    pending_meetings = Meeting.objects.filter(
        is_meeting_done= False).order_by("-pk").first()
         

    meeting_count = meetings.count() or 1 

    missed_meeting_percentage = ((meeting_count-attended_meeting)/meeting_count)*100  
    attended__meeting_percentage = 100- missed_meeting_percentage
    remaining_meetings = int(setting.number_of_meetings)- int(meeting_count)
    print("attended_meeting", attended_meeting)

    template = 'dashboard.html'
    context = {
        'user': request.user,
        'message': 'Welcome to your dashboard!',
        'remaining_meetings': range(remaining_meetings),
        'meetings':meetings,
        'pending_meetings':pending_meetings,
        'total_meetings': setting.number_of_meetings,
        'attended':attended__meeting_percentage,
        'absent': missed_meeting_percentage
    }
    return render(request, template, context)


@login_required
def meeting(request):

    setting,_ = AdminSetting.objects.get_or_create(pk =1)
    attended_meeting = Meeting.objects.filter(
        is_meeting_done= True, attendees = request.user).count() or 0

    meetings = Meeting.objects.filter(is_meeting_done= True)
    pending_meetings = Meeting.objects.filter(
        is_meeting_done= False).order_by("-pk").first()
         

    meeting_count = meetings.count() or 1 

    missed_meeting_percentage = ((meeting_count-attended_meeting)/meeting_count)*100  
    attended__meeting_percentage = 100- missed_meeting_percentage
    remaining_meetings = int(setting.number_of_meetings)- int(meeting_count)
   

    template = 'meeting.html'
    context = {
        'user': request.user,
        'message': 'Welcome to your dashboard!',
        'remaining_meetings': range(remaining_meetings),
        'meetings':meetings,
        'pending_meetings':pending_meetings,
        'total_meetings': setting.number_of_meetings,
        'attended':attended__meeting_percentage,
        'absent': missed_meeting_percentage
    }
    return render(request, template, context)




@login_required
def save_profile(request):
    if request.method == 'POST':
        # Retrieve data from the POST request
        first_name = request.POST.get('display_name')
        last_name = request.POST.get('last_name')
        phonenumber = request.POST.get('phone_number')
        new_password = request.POST.get('new_password')
        location = request.POST.get('location')
        church_branch = request.POST.get('church_branch')
        profession = request.POST.get('profession')
        message = request.POST.get('message')
        print("phonenumber", phonenumber)

        # Update the user's profile data
        user = request.user
        user.first_name = first_name
        user.last_name = last_name
        user.phonenumber = phonenumber
        user.location = location
        user.church_branch = church_branch
        user.profession = profession

        # Check if a new password is provided and update it if necessary
        if new_password:
            user.set_password(new_password)
        
        # Handle profile picture upload
        if 'profile_picture' in request.FILES:
            user.picture = request.FILES['profile_picture']

        # Save the updated user profile
        user.save()
        if message:
            return redirect('/dashboard')
        # Redirect to a success page or back to the profile page
        return redirect('/profile')  # Replace 'profile' with the name of your profile page URL pattern

    # Handle GET request or other cases where method is not POST
    return redirect('/profile')  # Redirect to the profile page if the method is not POST


@login_required
def profile(request, context=None):
    template = 'profile.html'
    if context is None:
        context = ''
    
    return render(request, template, context={"message":context, 'professions': professions})
