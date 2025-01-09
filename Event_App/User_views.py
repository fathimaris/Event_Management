import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from Event_App.forms import Customer_Reg, Event_Reg, Edit_Profile_form
from Event_App.models import Customer_Profile, Event_Booking, Payment


#------------------------------------------UserBase-----------------------------------------------------------------------------
def UserBase(request):
    return render(request,'User/UserBase.html')


#----------------------------------------ProfileView---------------------------------------------------------------------------
@login_required
def User_details(request):
    profile = Customer_Profile.objects.get(user=request.user)
    return render(request,'User/User_details.html',{'profile':profile})


#---------------------------------------Event Booking---------------------------------------------------------------------------


def Booking_Event(request):
    u = request.user
    data = Customer_Profile.objects.get(user=u)
    form1 = Customer_Reg(instance=data)
    form = Event_Reg()
    if request.method == 'POST':
        form1 = Customer_Reg(request.POST,instance=data)
        form = Event_Reg(request.POST)
        if form.is_valid() and form1.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            obj.save()
            return redirect('UserBase')
    return render(request,'User/Booking_Event.html',{'form': form,'form1':form1})



#--------------------------------------View for booked Event-------------------------------------------------------------------


def View_Booked_Event(request):
    data = Customer_Profile.objects.filter(user=request.user)
    data1 = Event_Booking.objects.filter(user=request.user)
    return render(request, 'User/View_Booked_Event.html', {'data': data,'data1':data1})






#--------------------------------------------Checkout/payment session----------------------------------------------------------

# views.py
import stripe
from django.conf import settings
from django.shortcuts import render, redirect

# Initialize Stripe with your secret key
stripe.api_key = settings.STRIPE_SECRET_KEY

def create_checkout_session(request):
    YOUR_DOMAIN = "http://localhost:8000"  # Change to your domain
    try:
        # Create a Stripe Checkout session
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',  # Adjust to your currency
                        'product_data': {
                            'name': 'Event Ticket',
                        },
                        'unit_amount': 10000,  # Fixed amount in cents
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/payment-success/',
            cancel_url=YOUR_DOMAIN + '/payment-cancel/',
        )

        return redirect(checkout_session.url, code=303)

    except Exception as e:
        return str(e)


def payment_success(request):
    return render(request, 'User/payment_success.html')

def payment_cancel(request):
    return render(request, 'User/payment_cancel.html')



#---------------------------------------Edit Profile---------------------------------------------------------------------------


def Edit_Profile(request):
    data = Customer_Profile.objects.get(user=request.user)
    form = Edit_Profile_form(instance=data)
    if request.method == 'POST':
        form = Edit_Profile_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('User_details')
    return render(request,'User/Edit_profile.html',{'form':form})