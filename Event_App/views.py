from django.contrib import messages, auth
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from Event_App.forms import User_Reg, Customer_Reg


# Create your views here.

#-------------------------------------------IndexPage________________________________________________________________________
def Index(request):
    return render(request,'index.html')
#-------------------------------------------Photo Gallery---------------------------------------------------------------------

def Gallery(request):
    return render(request,'Gallery.html')

#--------------------------------------------TESTIMONIAL--------------------------------------------------------------------

def Testimonials(request):
    return render(request,'Testimonials.html')


#-------------------------------------------COOPERATIVE EVENT----------------------------------------------------------------

def Cooperative_Event(request):
    return render(request,'Cooperative_event.html')

#-----------------------------------------------WEDDING VENUES---------------------------------------------------------------

def Wedding_Venue(request):
    return render(request,'Wedding_Venues.html')

#---------------------------------------------Register_________________________________________________________________________-


def Customer_Registration(request):
    form1 = User_Reg()  # Form for user account creation
    form2 = Customer_Reg()  # Form for customer profile creation

    if request.method == 'POST':
        # Populate forms with POST data and files (for file upload fields)
        form1 = User_Reg(request.POST)
        form2 = Customer_Reg(request.POST, request.FILES)

        # Validate both forms
        if form1.is_valid() and form2.is_valid():
            user = form1.save(commit=False)  # Create user object without saving
            user.is_customer = True  # Mark user as a customer
            user.save()  # Save user to database

            customer = form2.save(commit=False)  # Create customer object without saving
            customer.user = user  # Link customer profile to user
            customer.save()  # Save customer to database

            # Redirect to signin page with a success message
            messages.info(request, 'Customer registered successfully')
            return redirect('Login')

    # Render signup form page
    return render(request, 'Register.html', {'form1': form1, 'form2': form2})


#___________________________________________Login____________________________________________________________________________

def Login(request):
    if request.method == "POST":
        username = request.POST.get('username')  # Get the username from form
        password = request.POST.get('password')  # Get the password from form
        user = auth.authenticate(username=username, password=password)  # Authenticate user

        if user is not None and user.is_staff:  # Check if user is a staff member
            login(request, user)  # Log in the user
            return redirect('AdminBase')  # Redirect to admin page

        elif user is not None and user.is_customer:  # Check if user is a customer
            login(request, user)  # Log in the user
            return redirect('UserBase')  # Redirect to customer home page

        else:
            messages.info(request, 'Invalid Credentials')  # Show error message for invalid credentials

    return render(request, 'Login.html')  # Render login page if GET request or invalid credentials

#--------------------------------------Logout-----------------------------------------------------------------------------------


def Logout_view(request):
    logout(request)  # This logs out the user
    return redirect('index')