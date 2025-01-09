#--------------------------------------------------Admin Base-------------------------------------------------------------------
import datetime

from django.contrib.auth.decorators import user_passes_test

from Event_App.models import Event_Booking, Payment, Customer_Profile, Event
from django.contrib.auth import get_user_model
User = get_user_model()


def AdminBase(request):
    User = get_user_model()
    completed_payments_count = Payment.objects.filter(status="Completed").count()
    booking_count = Event_Booking.objects.count()
    user_count = User.objects.exclude(is_superuser=True).count()
    return render(request,'Admin/AdminBase.html',{'user_count': user_count,'booking_count': booking_count,'completed_payments_count': completed_payments_count})


#--------------------------------------------View Customers---------------------------------------------------------------------------


from .models import Customer_Profile
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def view_registered_users(request):
    # Retrieve profiles for all users except superusers
    customers = Customer_Profile.objects.filter(user__is_superuser=False)




    return render(request, 'Admin/view_registered_users.html', {'customers': customers})


#----------------------------Delete Customer----------------------------------------------------------------------------------


@user_passes_test(lambda u: u.is_superuser)
def Delete_customer(request, user_id):
    customer = get_object_or_404(Customer_Profile, user_id=user_id)
    customer.user.delete()  # This will delete both the user and the related profile
    return redirect('view_registered_users')


#------------------------------------------View Booked Event------------------------------------------------------------------


def view_registered_events(request):
    # Fetch all event bookings
    events = Event_Booking.objects.all()

    # Render the template with event data
    return render(request, 'Admin/view_registered_events.html', {'events': events})

#-------------------------------event approval---------------------------------------------------------------------------------

from django.shortcuts import get_object_or_404
from .models import Event_Booking

def approve_event(request, id):
    event = get_object_or_404(Event_Booking, id=id)
    event.Approval_Status = 1  # Set status to Approved
    event.save()
    return redirect('view_registered_events')  # Replace with your registered events view name

def reject_event(request, id):
    event = get_object_or_404(Event_Booking, id=id)
    event.Approval_Status = 2  # Set status to Rejected
    event.save()
    return redirect('view_registered_events')  # Replace with your registered events view name
#---------------------------------calendar--------------------------------------------------------------------------------------

# myapp/views.py
from django.shortcuts import render
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect

def calendar_view(request, year=None, month=None):
    # If no year/month provided, use the current date
    now = datetime.now()
    year = year or now.year
    month = month or now.month

    try:
        # Convert year and month to integers
        year = int(year)
        month = int(month)
    except ValueError:
        # Redirect to the current month if invalid input
        return HttpResponseRedirect('/calendar/')

    # Handle month overflow/underflow
    if month < 1:
        year -= 1
        month = 12
    elif month > 12:
        year += 1
        month = 1

    # Generate the calendar for the given month and year
    cal = HTMLCalendar().formatmonth(year, month)

    # Calculate previous and next month
    prev_month = month - 1 if month > 1 else 12
    prev_year = year - 1 if month == 1 else year
    next_month = month + 1 if month < 12 else 1
    next_year = year + 1 if month == 12 else year

    # Pass the calendar and navigation data to the template
    context = {
        'calendar': cal,
        'year': year,
        'month': month,
        'prev_year': prev_year,
        'prev_month': prev_month,
        'next_year': next_year,
        'next_month': next_month,
    }
    return render(request, 'Admin/Calendar.html', context)

