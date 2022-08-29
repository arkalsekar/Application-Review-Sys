from django.shortcuts import render, HttpResponse, redirect
from .models import Contact
from django.contrib import messages
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.decorators import login_required
import string 
import uuid 
import random 

# Create your views here.
def signup(request):
    if request.method=='POST':
        uname = request.POST['uname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['signupemail']
        password = request.POST['signuppassword1']
        password2 = request.POST['signuppassword2']

        # Checks for creating User
        if len(uname) < 3:
            messages.error(request, 'Username should be greater then 3')

        create_newuser = User.objects.create_user(uname, email, password2)
        create_newuser.first_name = fname
        create_newuser.last_name = lname
        create_newuser.save()
        messages.success(request, f'User {uname} created successfully, Go ahead and Login to your Account')

    return redirect('/')


def handle_login(request):
    if request.method=='POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']    

        user = authenticate(request, username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, f'Successfully Logged in as - {user}')
            return redirect('contact')
        else:
            messages.error(request, 'No Such User exists')
            return redirect('/')
    else:
        messages.error(request, f'{user} Details dont Match the Database Please Try Agians')
        return redirect('/')


@login_required
def handle_logout(request):
    if not request.user.is_authenticated:
        return redirect('/')
    logout(request)
    messages.success(request, f' Successfully Logged Out')
    return redirect('/')


def generate_user_id(n):    
    S = n # number of characters in the string.  
    # call random.choices() string module to find the string in Uppercase + numeric data.  
    ran = ''.join(random.choices(string.digits, k = S))
    return int(ran)   

def home(request):
    random_uid = generate_user_id(3)
    print(random_uid)
    return render(request, 'index.html')

@login_required
def contact(request):
    current_user_form = Contact.objects.filter(name=request.user)
    print(len(current_user_form))
    # print(random_uid)
    # print(i.user_id)
    if len(current_user_form) != 0:
        for i in current_user_form:
            pass

        messages.info(request, f"Your form has been already filled. Check your Status using your Application ID - {i.user_id}  ")
        return redirect('home')
        
    else: 
        if request.method == "POST":
            name = request.user
            email = request.POST['email']
            title = request.POST['title']
            desc = request.POST['desc']
            random_uid = generate_user_id(6)

            if name is not None:
                saving_the_form = Contact(name=name, email=email, title=title, desc=desc, accepted=False, user_id=random_uid)
                saving_the_form.save() 
                messages.success(request, "Form Filled Successfully")

    return render(request, 'contact.html')


def check_status(request):
    try:
        get_user_form = Contact.objects.filter(name=request.user)
        # print(get_user_form)
        for i in get_user_form:
            userid = int(i)
        
        context = {'users_info': userid}
    except:
        pass
    return render(request, 'status.html')    


def get_status(request):
    query = request.GET['Applicationid'] 
    if len(query) < 4:
        messages.info(request, "Invalid Application ID, Make sure Application ID is an integer")   
        context = {}
    # print(query)
    else:
        status = Contact.objects.filter(user_id=int(query))
    
        # print(len(status))
        if len(status) is not 0:
            messages.success(request, "We got your Application")
            no_status = True
            # return redirect('check_status')
            # print(context)
        else:
            messages.info(request, "We are unable to fetch your Application")
            no_status = True
            # return redirect('check_status')
        context = {'status': status, 'no_status': no_status}

    

    return render(request, 'status.html', context)
